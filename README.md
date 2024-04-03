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


## Motivation

The smallest unit of information in classical computing is the bit, which can take either the value of 0 or 1. However, in quantum computing, there exists the 'qubit'. A qubit is a unit of data that can be in a state of both 0 and 1 simultaneously. This phenomenon opens up a new world of computing possibilities.


### Project Summary

The main objective of this project is to ascertain what new inferences could be made about a dataset via Quantum Machine Learning (QML) when compared to classical Machine Learning (ML), and attempt to explain how these differences come about. This was achieved by using a common ML method, building an equivalent QML model, and making inferences about the data by measuring feature importance - that is, how important is a feature in making an accurate classification by using feature omission and permutations to quantify the differences. This is only the second paper on exploring the differences between how classical and quantum models prioritize features, and as of writing, this is the first project to fully explore the optimization of QML models in tandem with feature importance.

<img width="710" alt="image" src="https://github.com/LukePower01/ml-to-qml/assets/103632413/fd9a3f78-b0d0-470f-9c92-75f83350059c">


## Methodology

The approach to this project involved engaging in an in-depth course on quantum computing, gaining familiarity with concepts of quantum theory, and utilizing IBM's Qiskit platform, which provides access to quantum hardware and the necessary tools for building circuits and models. After exploratory scripts and demonstrations of basic quantum advantage, initial Quantum Machine Learning (QML) models were built and preliminary results documented.

## Concepts and Technologies

### Machine Learning

Machine Learning (ML) is a branch of computer science that uses statistical models to infer underlying patterns in a dataset and constructs algorithms capable of making accurate predictions or classifications with new, unseen data.

Machine Learning can be categorized into three main types:

- **Supervised Learning:** Models are trained on a labeled dataset, learning to predict outcomes for new data based on this training.
- **Unsupervised Learning:** Algorithms work with unlabeled data to find structure or patterns, without explicit instructions on how to process it.
- **Reinforcement Learning:** An agent learns to make decisions by taking actions in an environment to achieve some objectives, learning from rewards or penalties.

Supervised learning, the most commonly used form of machine learning, was the method utilized in this project. It involves training a model on data to minimize some cost function, thereby adjusting its parameters for better predictions.

### Qubits and Superposition

Quantum Machine Learning (QML) is a field of quantum computing that exploits quantum physics phenomena, such as superposition and entanglement, allowing for multiple computations to occur simultaneously. The '**qubit**' is the quantum equivalent of the classical computing bit. Unlike bits, which are strictly in one of two states (0 or 1), a qubit can exist in both states simultaneously, a phenomenon known as **superposition**.

![schrodingers_cat_cartoon](https://github.com/LukePower01/ml-to-qml/assets/103632413/389faee9-4c7e-4b1a-bcc0-1877d5ab242f)
Schrodinger's Cat serves as a quintessential example of quantum superposition, illustrated through a thought experiment where a cat is placed inside a sealed box with a radioactive element. This element has a 50% chance of decaying and releasing poison that would kill the cat. According to quantum mechanics, until the box is opened and the cat's state is observed (alive or dead), the cat is considered to be in a superposition of both states simultaneously. This concept underscores the principle that data in superposition allows a quantum algorithm to perform computations on multiple values at once, potentially leading to exponential computational speedups and the capacity to handle high-dimensional data.

### Feature Importance & Explainable ML

Machine Learning (ML) models, despite their wide application across various sectors, often function as 'black boxes', where the internal mechanisms remain opaque to users. Data is input, and results are output, with little understanding of the model's internal processes. This scenario has spurred interest in 'Explainable AI' (XAI) and Explainable ML, initiatives focused on demystifying the inner workings of models. For instance, being able to elucidate the reasons behind a denied loan application could be invaluable for transparency and trust.

#### Methods for Assessing Feature Importance:

- **Leave-One-Out (LOO) Feature Importance:** Evaluates the impact on model performance when each feature is omitted one at a time. A significant performance reduction without a specific feature indicates its importance.

- **Permutation Feature Importance:** Determines feature importance by observing the increase in the model's prediction error after permuting the feature's values, thereby disrupting the relationship between the feature and the outcome.

- **SHapley Additive exPlanations (SHAP) Values:** Rooted in cooperative game theory, SHAP values quantify each feature's contribution to a particular prediction, providing detailed insights into the model's decision-making process.

- **Partial Dependence Plots (PDPs):** These plots illustrate the average effect of a feature on the model's predictions, factoring out the influence of other features.

### Tech & Tools

#### IBM Qiskit

Qiskit is an open-source Quantum Software Development Kit (SDK) that enables users to engage with quantum algorithms and simulations. It offers tools for crafting and executing quantum computing programs on either actual quantum hardware or simulators, thus democratizing quantum computing for a wider audience.

#### Python

Python is a high-level programming language that is compatible with IBM Qiskit, renowned for its versatility, particularly in data science. One of Python's major strengths is its extensive library support coupled with an intuitive syntax, making it a preferred choice for many developers.

#### Jupyter Notebook

In this project, Jupyter Notebooks were leveraged for their integrated coding and documentation capabilities. They allow for code execution in segments paired with markdown annotations, facilitating reproducible results and streamlined reporting.

