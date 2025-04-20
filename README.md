# 🧪 Mini Hoop Simulador

Simula o comportamento básico da ferramenta **Hoop** usada em ambientes corporativos para acessar instâncias de clientes e executar comandos como `deal`, `ap`, entre outros.

Este projeto utiliza **Docker** e **Flask** para simular múltiplas instâncias com endpoints interativos.

---

## 🚀 Tecnologias

- Docker
- Flask (Python)
- Shell Script

---

## 🧰 Funcionalidades

- Subida de múltiplas instâncias com Docker
- Endpoints simulados (`/deal`, `/ap`)
- Comando `exec.sh` para simular `hoop exec`

---

## 📦 Subindo o projeto

1. Clone o repositório com SSH:

```bash
git@github.com:usuario/mini-hoop-simulador.git
cd mini-hoop-simulador
```

## Suba os containers:

```bash
docker compose up --build -d
```
## 🌐 Acessos locais:

Instância 1: http://localhost:5001
Instância 2: http://localhost:5002

## 🔧 Testes com curl:

```bash
curl localhost:5001/deal
curl localhost:5002/ap
```

## 🔁 Simular hoop exec

```bash
./exec.sh hoop_inst1 curl localhost:5000/deal
./exec.sh hoop_inst2 curl localhost:5000/ap
```

## 🛠️ Futuras melhorias

1. Simular autenticação
2. Adicionar logs por cliente
3. Interface interativa no terminal

## Feito com ❤️ para estudos e prática de ambientes simulados.


