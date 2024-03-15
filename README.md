
<p align="center" style="font-size: 140%;">
    <b>🧭 FedCompass - Efficient Cross-Silo Federated Learning with a Computing Power Aware Scheduler.</b>
</p>


<p align="center">
  <a href="https://discord.com/invite/bBW56EYGUS">
      <img src="https://dcbadge.vercel.app/api/server/bBW56EYGUS?theme=default-inverted&style=flat" alt="discord">
  </a>
  <a href="https://arxiv.org/abs/2309.14675">
      <img src="https://img.shields.io/badge/arXiv-2309.14675-B31B1B.svg" alt="paper">
  </a>
  <a href="https://openreview.net/forum?id=msXxrttLOi">
      <img src="https://img.shields.io/badge/OpenReview-FedCompass-FF00.svg" alt="project">
  </a>
  <a href="https://appfl.github.io/FedCompass/">
      <img src="https://img.shields.io/badge/project-FedCompass-B3FFF4.svg" alt="project">
  </a>
  <a href="./LICENSE">
      <img src="https://img.shields.io/badge/license-MIT-green?style=flat&logo=github" alt="project">
  </a>
</p>

<details>
  <summary><b>Table of Contents</b></summary>
  <p>

- [Introduction](#introduction)
- [Installation](#installation)
- [Launch Experiment](#launch-first-example-experiment)
    - [Serial Simulation](#serial-simulation)
    - [MPI Simulation](#mpi-simulation)
    - [gRPC Deployment](#grpc-deployment)
- [Features](#features)
- [Citations](#citation)

  </p>
</details>

### Introduction
FedCompass is a semi-asynchrnous federated learning (FL) algorithm which addresses the time-efficiency challenge of other synchronous FL algorithms, and the model performance challenge of other asynchronous FL algorithms (due to model stalenesses) by using a *COM*puting *P*ower *A*ware *Scheduler* *(COMPASS)* to adaptively assign different numbers of local steps to different FL clients and synchrnoize the arrival of client local models. 

This repository is built upon the open-source and highly extendible FL framework [APPFL](https://github.com/APPFL/APPFL) and employs gRPC as the communication protocol to help you easily launch FL experiment using FedCompass among distributed FL clients.

### Installation
Users can install by cloning this repository and installing the package locally. We also highly recommend to create a virtual environment for easy dependency management.
```bash
conda create -n fedcompass python=3.8
conda activate fedcompass
git clone https://github.com/APPFL/FedCompass.git && cd FedCompass
pip install -e .
```

### Launch First Example Experiment
In the `examples` folder, we provide example scripts to train a CNN on the MNIST dataset using federated learning by running [serial simulation](#serial-simulation), [MPI simulation](#mpi-simulation), and [gRPC deployment](#grpc-deployment). Specifically, in this repository, we refer

- **simulation** as federated learning experiments that can only run on a single machine or a cluster
- **deployment** as federated learning experiments that can run only multiple distributed machines

#### Serial Simulation

Please go to the `examples` folder first, and then run the following command
```bash
python serial/run_serial.py \
    --server_config config/server_fedavg.yaml \
    --client_config config/client_1.yaml \
    --num_clients 5
```
where `--server_config` is the path to the configuration file for the FL server. We currently provide three configuration files for the FL server, corresponding to three different FL algorithms. However, it should be noted at the beginning that serial simulation is only suitable and making sense for synchrnous federated learning algorithms. 
- `config/server_fedcompass.yaml`: FL server for the FedCompass algorithm
- `config/server_fedavg.yaml`: FL server for the FedAvg algorithm
- `config/server_fedasync.yaml`: FL server for the FedAsync algorithm

`--client_config` is the path to the base configuration file for the FL clients, and `--num_clients` is the number of FL clients you would like to simulate.

#### MPI Simulation
Please go to the `examples` folder first, and then run the following command
```bash
mpiexec -n 6 python mpi/run_mpi.py \
    --server_config config/server_fedcompass.yaml \
    --client_config config/client_1.yaml 
```
where `mpiexec -n 6` means that we start 6 MPI processes, and there will be 6-1=5 FL clients, as one MPI process will serve as the FL server.

#### gRPC Deployment

Please go to the `examples` folder first. To launch a server, users can run the following command, 
```bash
python grpc/run_server.py --config config/server_fedcompass.yaml
```

The above command launches an FL server at `localhost:50051` waiting for connection from two FL clients. To launch two FL clients, open two separate terminals and go to the `examples` folder, and run the following two commands, respectively. This will help you start an FL experiment with two clients and a server running the specified algorithm.
```bash
python grpc/run_client_1.py
```
```bash
python grpc/run_client_2.py
```

### Features

- [x] Server aggregation algorithm customization
- [x] Server scheduling algorithm customization
- [x] Client local trainer customization
- [x] Synchronous federated learning
- [x] Asynchronous Federated Learning
- [x] Semi-asynchronous federated learning
- [x] Model and dataset customization
- [x] Loss function and evaluation metric customization
- [x] Heterogeneous data partition
- [x] Lossy compression using SZ compressors
- [x] Single-node serial federated learning simulation
- [x] MPI federated learning simulation
- [x] Real federated learning deployment using gRPC
- [x] Authentication in gRPC using Globus Identity
- [ ] wandb visualization

### Citation
If you find FedCompass and this repository useful to your research, please consider cite the following paper
```
@article{li2023fedcompass,
  title={FedCompass: Efficient Cross-Silo Federated Learning on Heterogeneous Client Devices using a Computing Power Aware Scheduler},
  author={Li, Zilinghan and Chaturvedi, Pranshu and He, Shilan and Chen, Han and Singh, Gagandeep and Kindratenko, Volodymyr and Huerta, Eliu A and Kim, Kibaek and Madduri, Ravi},
  journal={arXiv preprint arXiv:2309.14675},
  year={2023}
}
```

```
@inproceedings{ryu2022appfl,
  title={APPFL: open-source software framework for privacy-preserving federated learning},
  author={Ryu, Minseok and Kim, Youngdae and Kim, Kibaek and Madduri, Ravi K},
  booktitle={2022 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)},
  pages={1074--1083},
  year={2022},
  organization={IEEE}
}
```
