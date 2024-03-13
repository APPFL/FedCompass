from omegaconf import OmegaConf
from appfl.agent import APPFLClientAgent
from appfl.comm.grpc import GRPCClientCommunicator

max_message_size = 1024 * 1024

client_agent_config = OmegaConf.load("config/client_2.yaml")

client_agent = APPFLClientAgent(client_agent_config=client_agent_config)
client_comm = GRPCClientCommunicator(
    client_id = client_agent.get_id(),
    **client_agent_config.comm_configs,
)

client_config = client_comm.get_configuration()
client_agent.load_config(client_config)

init_global_model = client_comm.get_global_model(init_model=True)
client_agent.load_parameters(init_global_model)

# Send the number of local data to the server
sample_size = client_agent.get_sample_size()
print(f"Sample size: {sample_size}")
client_comm.invoke_custom_action(action='set_sample_size', sample_size=sample_size)

for i in range(10):
    client_agent.train()
    local_model  = client_agent.get_parameters()
    new_global_model = client_comm.update_global_model(local_model)
    if isinstance(new_global_model, tuple):
        new_global_model, metadata = new_global_model[0], new_global_model[1]
        client_agent.trainer.train_configs.num_local_steps = metadata['local_steps']
    client_agent.load_parameters(new_global_model)