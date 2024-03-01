import argparse
from omegaconf import OmegaConf
from appfl.agent import APPFLServerAgent
from appfl.comm.grpc import GRPCServerCommunicator, serve

argparser = argparse.ArgumentParser()
argparser.add_argument(
    "--config", 
    type=str, 
    default="config/server_fedcompass.yaml",
    help="Path to the configuration file."
)
args = argparser.parse_args()

max_message_size= 1024 * 1024

server_agent_config = OmegaConf.load(args.config)
server_agent = APPFLServerAgent(server_agent_config=server_agent_config)

communicator = GRPCServerCommunicator(server_agent, max_message_size=max_message_size)
serve(communicator, max_message_size, server_uri="localhost:50051")