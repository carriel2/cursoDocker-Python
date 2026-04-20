import docker

client = docker.DockerClient(base_url="unix://var/run/docker.sock")

for event in client.events():
    print(event)
