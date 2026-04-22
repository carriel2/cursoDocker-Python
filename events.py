import docker
import datetime
import requests

client = docker.DockerClient(base_url="unix://var/run/docker.sock")
webhook_url = "https://discord.com/api/webhooks/1496473445020602539/88NuoFcHJXB38N01OoCVdMb-cky3CYTD42aw20jw0R6FSDJayfc6L8NjQRZnXLF_myp_"

for event in client.events(decode=True, filters={"event": "die"}):
    container_id = event["Actor"]["ID"]
    container_name = event["Actor"]["Attributes"]["name"]
    epoch_time = event["time"]
    date_time  = datetime.datetime.fromtimestamp(epoch_time)
    
    payload = {"content": "Informação: O container %s (%s) foi finalizado às %s" % (container_name, container_id, date_time)}
    
    print (payload)
    requests.post(webhook_url, data=payload)