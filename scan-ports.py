from pykube import HTTPClient, Service

api = HTTPClient(kubeconfig="caminho/para/seu/kubeconfig")

services = Service.objects(api)

portas_expostas = []

for service in services:

    if service.obj['spec'].get('type') == 'NodePort':
        portas = service.obj['spec']['ports']
        for porta in portas:
            portas_expostas.append(porta['nodePort'])

print(portas_expostas)
