from omegaconf import OmegaConf
from appfl.agent import APPFLServerAgent
from appfl.comm.grpc import GRPCServerCommunicator, serve

max_message_size= 1024 * 1024

server_agent_config = OmegaConf.load("config/server_fedcompass.yaml")
server_agent = APPFLServerAgent(server_agent_config=server_agent_config)

communicator = GRPCServerCommunicator(server_agent, max_message_size=max_message_size)
serve(communicator, max_message_size)