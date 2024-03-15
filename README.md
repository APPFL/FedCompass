
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

- [Introduction](#🎙-introduction)
- [Installation](#⚙️-installation)
- [Launch Experiment](#🚀-launch-first-example-experiment)
- [Features](#🔥-features)
- [Citations](#📃-citation)

  </p>
</details>

### 🎙 Introduction
FedCompass is a semi-asynchrnous federated learning (FL) algorithm which addresses the time-efficiency challenge of other synchronous FL algorithms, and the model performance challenge of other asynchronous FL algorithms (due to model stalenesses) by using a *COM*puting *P*ower *A*ware *Scheduler* *(COMPASS)* to adaptively assign different numbers of local steps to different FL clients and synchrnoize the arrival of client local models. 

This repository is built upon the open-source and highly extendible FL framework [APPFL](https://github.com/APPFL/APPFL) and employs gRPC as the communication protocol to help you easily launch FL experiment using FedCompass among distributed FL clients.

### ⚙️ Installation
Users can install by cloning this repository and installing the package locally. We also highly recommend to create a virtual environment for easy dependency management.
```bash
conda create -n fedcompass python=3.8
conda activate fedcompass
git clone https://github.com/APPFL/FedCompass.git && cd FedCompass
pip install -e .
```

### 🚀 Launch First Example Experiment
Please go to the `examples` folder first. To launch a server, users can run the following command, 
```bash
python grpc/run_server.py --config config/server_fedcompass.yaml
```
where `--config` is the path to the configuration file. We currently provide three configuration files for the FL server, corresponding to three different FL algorithms
- `config/server_fedcompass.yaml`: FL server for the FedCompass algorithm
- `config/server_fedavg.yaml`: FL server for the FedAvg algorithm
- `config/server_fedasync.yaml`: FL server for the FedAsync algorithm

The above command launches an FL server at `localhost:50051` waiting for connection from two FL clients. To launch two FL clients, open two separate terminals and go to the `examples` folder, and run the following two commands, respectively. This will help you start an FL experiment with two clients and a server running the specified algorithm.
```bash
python grpc/run_client_1.py
```
```bash
python grpc/run_client_2.py
```

### 🔥 Features

- [x] Server scheduling algorithm customization
- [x] Server aggregation algorithm customization
- [x] Client local trainer customization
- [x] Synchronous federated learning
- [x] Asynchronous Federated Learning
- [x] Semi-asynchronous federated learning
- [x] Model and dataset customization
- [x] Loss function and evaluation metric customization
- [x] Data heterogeneity
- [ ] wandb visualization
- [ ] Support for leaf-related datasets

### 📃 Citation
If you find FedCompass and this repository useful to your research, please consider cite the following paper
```
@article{li2023fedcompass,
  title={FedCompass: Efficient Cross-Silo Federated Learning on Heterogeneous Client Devices using a Computing Power Aware Scheduler},
  author={Li, Zilinghan and Chaturvedi, Pranshu and He, Shilan and Chen, Han and Singh, Gagandeep and Kindratenko, Volodymyr and Huerta, Eliu A and Kim, Kibaek and Madduri, Ravi},
  journal={arXiv preprint arXiv:2309.14675},
  year={2023}
}
```
