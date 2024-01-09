import os
import json
import requests

def check_dockerhub_for_new_image(event, context):
    # Define the Docker Hub repository URL
    repository_url = "https://hub.docker.com/v2/repositories/appdynamics/cluster-agent/tags/"

    # Get the latest image tags from Docker Hub
    try:
        response = requests.get(repository_url)
        response.raise_for_status()
        dockerhub_data = response.json()

        # Extract the list of available tags
        tags = [entry["name"] for entry in dockerhub_data.get("results", [])]

        # Find the index of "latest" in the list of tags
        latest_index = tags.index("latest")

        # Check if "latest" is not the latest tag and retrieve the next tag
        if latest_index < len(tags) - 1:
            next_tag = tags[latest_index + 1]
            print(f"Next image tag after 'latest': {next_tag}")
        else:
            print("No new image tag detected after 'latest'.")

    except Exception as e:
        print(f"Error: {str(e)}")

# If running locally, call the function to check for the next image tag after "latest"
if __name__ == "__main__":
    check_dockerhub_for_new_image(None, None)

