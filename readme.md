Esse script se baseia nas informações fornecidas pelos serviços Kubernetes e só mostrará as portas expostas para serviços do tipo NodePort

Antes de rodar o script, instale o pacote pykube-ng se ainda não o tiver instalado, utilizando o comando:

$ pip install pykube-ng

E depois e so baixar e rodar o " SCRIPT " ele exibirá a lista de portas expostas no cluster Kubernetes. 
Lembre-se de ter o kubeconfig corretamente configurado no arquivo ou passar o caminho para o kubeconfig usando kubeconfig="caminho/para/seu/kubeconfig" dentro do arquivo: scan-ports.py


*** Modo alternativo de instalar o PYKUBE-NG:

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python3 get-pip.py

