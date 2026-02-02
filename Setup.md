# ⚙️ Project Setup – Mini Docker Runtime (Python)

Follow these steps to run the project.

---

## 1. Go to project folder

```
cd ~/project/mini-docker-py
```

---

## 2. Create required directories

```
mkdir -p images containers logs
```

---

## 3. Check Python

```
python3 --version
```

Python 3.x required.

---

## 4. Build an image

```
python3 mini_docker.py build benimg
```

This creates an image inside `images/`.

---

## 5. Run a container

```
python3 mini_docker.py run benimg c1
```

You will enter an isolated shell.

Inside container you can run:

```
./hello.sh
```

Exit:

```
exit
```

---

## 6. Useful commands

List:
```
python3 mini_docker.py list
```

Logs:
```
python3 mini_docker.py logs c1
```

Remove:
```
python3 mini_docker.py rm c1
```

---

## Done

The mini container runtime is ready to use.
