import docker

client = docker.DockerClient(base_url="unix://var/run/docker.sock")

for event in client.events(decode=True, filter={"event": "die"}):
    print(event)
