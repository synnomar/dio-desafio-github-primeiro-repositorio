Git (https://git-scm.com/downloads)

#Gera a chave criptografada em SHA1
openssl sha1 nomedoarquivo.py

Objetos de versionamento no GIT
Blobs, Trees e Commits

blobs - contem meta dados 
Tree - Arvore aponta para os  blobs, responsavel de montar toda a estrutura.

# remover configurações no arquivo conf do git (necesasario quanto troca o dono da maquina) 
git config --global --unset user.email
git config --global --unset user.name

# Identificar o usuario do git na maquina para Identificação nos commit.
git config --global user.email "emais do usuario"
git config --global user.name "nome do usuario"

# Gerar chave criptografada para github --> enviar os arquivos para gothub
ssh-keygen -t ed25519 -C synnomar@hotmail.com


cd /c/Users/Usuario/.ssh/
ls
cat id_ed25519.pub
eval $(ssh-agent -s)
ssh-add id_ed25519

 git init

 git add *

(git add. ou git add -a)

 git commit -m "commit inicial"

# Enviar os arquivos commitados Local para a area Remota
git remote add origin git@github.com:synnomar/TesteGuit.git

#verificar os Branch remotos
git remote -v

# Verificar os Status 
git status

# Enviar todos os commits para o repositorio remoto. 
git push origin main




