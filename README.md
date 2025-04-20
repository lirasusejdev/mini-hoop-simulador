# 🧪 Mini Hoop Simulador

Simula o comportamento básico da ferramenta **Hoop** usada em ambientes corporativos para acessar instâncias de clientes e executar comandos como `deal`, `ap`, entre outros.

Este projeto utiliza **Docker** e **Flask** para simular múltiplas instâncias com endpoints interativos.

---

Infelizmente, não dá para instalar o Hoop de forma independente para estudos locais — o Hoop é uma ferramenta corporativa fechada, desenvolvida pela Trybe (ou usada por ela e outras empresas), e depende de uma infraestrutura de autenticação e permissões conectada à conta da empresa (como AWS, Okta, Vault etc).

🧩 Por que não dá pra usar em casa?

Ele é feito para ambientes controlados (produção/staging de empresas)

Depende de acesso a contas AWS, instâncias, secrets e vaults

Usa um cliente autenticador vinculado à empresa (por ex: SSO corporativo)



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


