# 🚀 Mini Docker Runtime in Python

A lightweight Docker-like container runtime built using Python.

This project simulates how Docker works internally by implementing:
- Image creation
- Container creation
- File isolation
- Command execution
- Logging
- CLI management

It is designed for learning Docker internals and Linux container concepts without requiring kernel privileges.

---

## 📦 Features

✅ Build images  
✅ Run containers  
✅ Isolated working directory  
✅ Interactive shell  
✅ Logs  
✅ List images/containers  
✅ Remove containers  

---

## 🧠 How It Works

Conceptually:

Image → Container → Execute

1. Image = template folder  
2. Container = copy of image  
3. Run = open bash inside isolated directory  

This mimics how Docker creates containers from images.

---

## 📁 Project Structure

```
mini-docker-py/
│
├── mini_docker.py
├── images/
├── containers/
├── logs/
└── README.md
```

---

## ⚙️ Setup

Clone:

```
git clone <your-repo>
cd mini-docker-py
```

Python:

```
python3 --version
```

No external dependencies required.

---

## 🚀 Usage

### Build image
```
python3 mini_docker.py build myimg
```

### Run container
```
python3 mini_docker.py run myimg c1
```

### List
```
python3 mini_docker.py list
```

### Logs
```
python3 mini_docker.py logs c1
```

### Remove
```
python3 mini_docker.py rm c1
```

---

## 🎯 Learning Goals

This project helps understand:

- How Docker images work
- How containers are created
- Isolation concepts
- Runtime management
- CLI tool design
