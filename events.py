import docker

client = docker.DockerClient(base_url="unix://var/run/docker.sock")

for event in client.events(decode=True, filters={"event": "die"}):
    container_id = event["Actor"]["ID"]
    container_name = event["Actor"]["Attributes"]["name"]
    epoch_time = event["time"]
    print ("O container %s (%s) foi finalizado às %s" % (container_name, container_id, epoch_time))