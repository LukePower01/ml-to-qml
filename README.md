# ml-to-qml
Final year project, exploring the field of quantum machine learning.

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Project Objectives](#my-project-objectives)


## Installation
Instructions on setting up the environment to run your notebooks. Include steps to clone the repo, install dependencies (`requirements.txt`) and any additional setup needed.

```bash
git clone https://github.com/LukePower01/ml-to-qml.git
cd ml-to-qml
pip install -r requirements.txt
```

## My Project Objectives
The focus of this project is to learn and the fundamental principles of QML, and to investigate what new inferences can be maade about classical data, that cannot be made with classical machine learning. 
<img width="710" alt="image" src="https://github.com/LukePower01/ml-to-qml/assets/103632413/fd9a3f78-b0d0-470f-9c92-75f83350059c">
This will involve: 
- Investage the classical data in a normal manner
- Encode the classical features and labels to a quantum state representation
- Implement QML techniques and a method of measuring feature importance
- Compare and contrast the rankings of features by classical and quantum methods. 

## Quantum Machine Learning
Quantum Machine Learning (QML) expands what is capabble by classical computers by utillizing phenomenom found in quantum physics, such as entanglement and superposition. 

## The Qubit                  
![The Bloch Sphere - Representation of the qubit](https://github.com/LukePower01/ml-to-qml/assets/103632413/a732ebb9-ec0a-4cfe-88da-ff03da6da82c)
The qubit is the quantum computing equivalent of the bit. What makes a qubit so special is that unlike a bit which is constrained to values of either 0 or 1, a qubit can be _simultaneously_ in 0 **and** 1 at the same time in a state called superposition.


# Introduction

## Motivation

The smallest unit of information in classical computing is the bit, which can take either the value of 0 or 1. However, in quantum computing, there exists the 'qubit'. A qubit is a unit of data that can be in a state of both 0 and 1 simultaneously. This phenomenon opens up a new world of computing possibilities.

## Project Summary & Document Outline

### Project Summary

The main objective of this project is to ascertain what new inferences could be made about a dataset via Quantum Machine Learning (QML) when compared to classical Machine Learning (ML), and attempt to explain how these differences come about. This was achieved by using a common ML method, building an equivalent QML model, and making inferences about the data by measuring feature importance - that is, how important is a feature in making an accurate classification by using feature omission and permutations to quantify the differences. This is only the second paper on exploring the differences between how classical and quantum models prioritize features, and as of writing, this is the first project to fully explore the optimization of QML models in tandem with feature importance.

![QML Approaches](images/Qml_approaches.png "This project involves using quantum algorithms on classical data. Image adapted from Schroedinger's Cat Cartoon.")

### Document Outline

This section provides an explanation of what is in the rest of the introduction and the contents of the rest of the chapters. The rest of the Introduction will provide a general overview of the project, the main objective, as well as some light background into the main concepts and technologies that were used.

