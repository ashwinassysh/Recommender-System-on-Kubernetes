# Recommender System for Team Assignment
This is a system that is intended to provide managers with recommendations on employees, for certain roles, that they could consider when forming a team. This repository is a step by step guide for implementing this system.

## Problem Statement and Motivation
Globalization and other trends have changed the business landscape, introducing new challenges and opportunities. From the same relationship, clients now expect more. Competition in markets has also become more aggressive. Further, individual expertise is getting more specialized, with the popularity of pursuing graduate and doctoral studies dramatically increasing. Companies are also expanding geographically, and the need for interdependence is higher than ever.
In such a collaboration economy, the role of managers has shifted from being primarily responsible for making command decisions based on information gathered from their subordinates. 
Their new role now involves identifying the key resources that will best implement the team’s objectives and then to facilitate the coordination of those resources.Our proposition aims to be an ‘enabler’ in this new role of ‘managers’ – to help them identify employees that could be a good fit for roles in a team that a manager is looking to fill.

## Decision-Making scenarios
As a solution, we look to enable the manager in decision-making in two scenarios –
1. A team manager wants to staff a given employee in a new role, and wants to figure out what roles the employee could perform well in.
2. The manager has a team profile (number of team members as well as roles) that he needs to build a team around.

## Benefits of the solution
Our solution is a more scientifically-backed approach to team assignment, rather than the traditional reliance on intuition.
This also reduces subjective bias (such as gender, race, etc.) that may creep into the selection process.
Our solution isn’t meant to eliminate the role of the manager in the team selection process, but to enable him with recommendations that he can further investigate. Thus, manager intervention is only needed at a later stage, until then allows focus other critical decisions.
Assessing suitability of roles for employees is no longer restricted to past roles he/she has done well in, our solution also recommends new roles he/she may excel in.
Enabling employees to experiment with other roles may also improve employee motivation and job satisfaction.

## DotA 2 Motivation
“Sports traditionally an excellent setting to examine teams” – for reasons such as the consistency of rules, clarity of outcomes, repeated observations, and behaviors at the levels of individuals and groups.
“Comparison tends to fail in contemporary organizations” – work becomes increasingly distributed, virtual, self-assembled, cross-functional, and fluid/temporary.
Why MOBA?  - employ a number of cooperative game design patterns that require players to employ complementary characters, shared goals, and synergistic abilities. People are also building expertise with respect to certain heroes/characters, while also working on interdependence and team synergy to get the best results. Additionally, data regarding Dota was readily available, unlike employee performance details that are internal to the organization.

## DotA 2 Context
1. Two team, 5v5 player game, objective is to destroy opposition base.
2. Players choose heroes, each hero can play multiple roles.
3. Player can improve hero capability by collecting items and resources through course of game.

## Kubeflow

Practically speaking, some of the biggest challenges facing ML applications are composability, portability, and scalability. The Kubernetes framework is well suited to address these issues, which is why it’s a great foundation for deploying ML products. Kubeflow is designed to take advantage of these benefits.

Kubeflow makes it easy for everyone to develop, deploy, and manage portable, scalable ML everywhere and supports the full lifecycle of an ML product, including iteration via Jupyter notebooks. It removes the need for expertise in a large number of areas, reducing the barrier to entry for developing and maintaining ML products. The composability problem is addressed by providing a single, unified tool for running common processes such as data ingestion, transformation, and analysis, model training, evaluation, and serving, as well as monitoring, logging, and other operational tools. The portability problem is resolved by supporting the use of the entire stack either locally, on-premise, or on the cloud platform of your choice. Scalability is native to the Kubernetes platform and leveraged by Kubeflow to run all aspects of the product, including resource-intensive model training tasks.

## Jupyter Notebook in Kubeflow
There are multiple benefits of integrating Jupyter notebooks in Kubeflow for enterprise environments. These benefits include:

Integrating well with the rest of the infrastructure with respect to authentication and access control.
Enabling easier notebook sharing across the organization. Users can create notebook containers or pods directly in the cluster, rather than locally on their workstations. Admins can provide standard notebook images for their organization, and set up role-based access control (RBAC), Secrets and Credentials to manage which teams and individuals can access the notebooks.
Overall, Kubeflow-hosted notebooks are better integrated with other components while providing extensibility for notebook images.

## Kubeflow on Google Cloud Platform (GCP)
Google Cloud Platform (GCP) is a suite of cloud computing services running on Google infrastructure. The services include compute power, data storage, data analytics, and machine learning.

The Cloud SDK is a set of tools that you can use to interact with GCP from the command line, including the gcloud command and others.

Kubernetes Engine (GKE) is a managed service on GCP where you can deploy containerized applications. You describe the resources that your application needs, and GKE provisions and manages the underlying cloud resources.

## Step-by-step setup guide
#### 1. Set up your GCP account and SDK
Follow these steps to set up your GCP environment:

      a. Select or create a project on the GCP Console.
      b. Make sure that billing is enabled for your project. See the guide to modifying a project’s billing settings.
      c. Install the Cloud SDK. If you already have the SDK installed, run gcloud components update to get the latest versions of the SDK tools.

#### 2. Install Docker
Follow the [Docker installation guide](https://docs.docker.com/install/)

#### 3. Install kubectl
Run the following Cloud SDK command to install the kubectl command-line tool for Kubernetes:
      gcloud components install kubectl

#### 4. Install kustomize
Install kustomize v2.0.3. See the [kustomize installation guide](https://github.com/kubernetes-sigs/kustomize/blob/master/docs/INSTALL.md)

#### 5. Set up environment variables
      a. Set your GCP project ID. In the command below, replace <YOUR-PROJECT-ID> with your project ID:

      export PROJECT=<YOUR-PROJECT-ID>
      gcloud config set project ${PROJECT}

      b. Set the zone for your GCP configuration. Choose a zone that offers the resources you need. 

      c. Set the DEPLOYMENT_NAME environment variable.export DEPLOYMENT_NAME=kubeflow

#### 6. Deploy Kubeflow using UI

      a. Open https://deploy.kubeflow.cloud/ in your web browser. You should see a form like the one in the above screenshot.
      b. Sign in to your browser using an account that has the owner role for your GCP project.
      c. Complete the following fields on the form:
            Project ID: Enter your GCP project ID.
            Deployment name: Enter a short name that you can use to recognize this deployment of Kubeflow. The maximum length for the deployment name is 25 characters.
            Choose how to connect to Kubeflow service: You can choose one of the following options:

      d. Login with GCP IAP: Choose this option if you want to use Cloud Identity-Aware Proxy (Cloud IAP) for access control. Cloud IAP is the best option for production deployments or deployments with access to sensitive data. See more details below.
      e. Login with Username Password: Choose this option if you want to allow users to access Kubeflow with a username and password, that is, with basic authentication. See more details below.
      f. GKE zone: Enter the GCP zone in which to create your deployment. The default is us-central-1a.

      g. Kubeflow version: Choose one of the available versions of Kubeflow. You can see all the versions on the Kubeflow releases page. If you need a version that does not show on the deployment UI, you need to deploy Kubeflow using the CLI.

      h. Share Anonymous Usage Report: Check this option to allow Kubeflow to report usage data using Spartakus. Spartakus does not report any personal information. The default is to enable the reporting of usage data.

      i. Click Create Deployment.

      j. Watch for the deployment updates in the information box at the bottom of the deployment UI.
      
![Deploy Kubeflow cluster on GCP](https://github.com/MainakRoy93/Recommender-System-on-Kubernetes/blob/master/Screenshots/kubeflow%20deployment.png?raw=true "Optional Title")


#### 7. Connect to the Kubeflow cluster
When the cluster is ready, you can do the following:

      a. Connect your local kubectl session to the cluster:
      gcloud container clusters get-credentials \
          ${DEPLOYMENT_NAME} --zone ${ZONE} --project ${PROJECT}

      b. Switch to the kubeflow namespace to see the resources on the Kubeflow cluster:
      kubectl config set-context $(kubectl config current-context) --namespace=kubeflow

      c. Check the resources deployed in the kubeflow namespace:
      kubectl get all

      d. Access the Kubeflow UI, which becomes available at the following URI after several minutes:
      https://<deployment-name>.endpoints.<project>.cloud.goog/
  
#### 8. Create a Cloud Storage bucket
      Cloud Storage is a scalable, fully-managed object/blob store. You can use it for a range of scenarios including serving website content, storing data for archival and disaster recovery, or distributing large data objects to users via direct download.

      Use the gsutil mb command to create a storage bucket. Your bucket name must be unique across all of Cloud Storage.
      export BUCKET_NAME=${PROJECT}-${DEPLOYMENT_NAME}-bucket
      gsutil mb -c regional -l us-central1 gs://${BUCKET_NAME}
      
![GCP Storage Bucket](https://github.com/MainakRoy93/Recommender-System-on-Kubernetes/blob/master/Screenshots/google%20cloud%20storage.png?raw=true "Optional Title")

#### 9. Create a new Jupyter Notebook and deploy code in the pipeline

      a. Click Notebook Servers in the left-hand panel of the Kubeflow UI.
      b. Choose the namespace corresponding to your Kubeflow profile.
      c. Click NEW SERVER to create a notebook server.
      d. Select a Docker image for the baseline deployment of your notebook server. You can choose from a range of standard images or specify a custom image
      e. When the notebook server provisioning is complete, click CONNECT.
      f. Click Upload to upload an existing notebook, or click New to create an empty notebook.
      
![Kubeflow UI dashboard](https://github.com/MainakRoy93/Recommender-System-on-Kubernetes/blob/master/Screenshots/kubeflow%20UI%20dashboard.png?raw=true "Optional Title")

#### 10. Clean up your GCP environment once the code is no longer required
Run the following command to delete your deployment and related resources

      gcloud deployment-manager --project=${PROJECT} deployments delete ${DEPLOYMENT_NAME}

Delete your Cloud Storage bucket when you’ve finished with it:

      gsutil rm -r gs://${BUCKET_NAME}

Delete the container images uploaded to Container Registry:

      // Find the digest id for each container image:
      gcloud container images list-tags gcr.io/${PROJECT}/${DEPLOYMENT_NAME}-train
      gcloud container images list-tags gcr.io/${PROJECT}/${DEPLOYMENT_NAME}-web-ui

      // Delete each image:
      gcloud container images delete gcr.io/$PROJECT/${DEPLOYMENT_NAME}-train:$DIGEST_ID
      gcloud container images delete gcr.io/$PROJECT/${DEPLOYMENT_NAME}-web-ui:$DIGEST_ID

## Requirements and Outputs of the recommendation system.
The recommendation system code requires the following:

      1. CSV and JSON files, present in the Sample Data Folder.
      2. Preferably an API key from OpenDota.com to collect data. Not having an API key may result in the code not returning results   to due hitting the maximum cap on the number of requests that can be made in the free API version.
      
Program Outputs:
For the purposes of the demo, we randomly choose 20 of the 1194 professional DOTA2 players in the dataset.

      1.Calculating similar players and hero recommendations: 
      
            a. This returns the best heroes played by the random set of players.
            b. Players found to similar to each player.            
            c. Hero recommendations as calculated by the Pearson Co-relation Coefficient.
![Hero Recommendations](https://github.com/MainakRoy93/Recommender-System-on-Kubernetes/blob/master/Screenshots/2019-12-09_01h23_22.png?raw=true "Optional Title")

      2.Team Recommendations: To calculate the best team from the available players requires the team profile to me given as an input.This can be done by resetting the default values of the dictionary ‘role_dict’.

            a.Returns the best team that can be created using the team profile given as input.   
            b.Returns player role and heroes that they should play.    
            c.Some in-game characteristics of the selected players.   
            d.Average team in-game characteristics in the form of visualizations.
![Team](https://github.com/MainakRoy93/Recommender-System-on-Kubernetes/blob/master/Screenshots/2019-12-09_00h59_28.png?raw=true "Optional Title")
![Visualizations](https://github.com/MainakRoy93/Recommender-System-on-Kubernetes/blob/master/Screenshots/2019-12-09_00h58_45.png?raw=true "Optional Title")
## Resources used
1. https://www.kubeflow.org/docs/gke/gcp-e2e/
2. https://www.kubeflow.org/docs/gke/deploy/project-setup/
3. https://conferences.oreilly.com/strata/strata-ny-2018/public/schedule/detail/69041
4. https://www.kubeflow.org/docs/notebooks/why-use-jupyter-notebook/
5. https://github.com/dangkhoadl/Dota2-Hero-Recommendation

## Contributors

[Arnav Sivaram](https://www.linkedin.com/in/arnav-sivaram/) - sivar031@umn.edu

[Ashwin Sharma](https://www.linkedin.com/in/ashwinassysh/) - sharm702@umn.edu

[Mainak Roy](https://www.linkedin.com/in/mainak-roy/)  - roy00083@umn.edu

[Sameeksha Aithal](https://www.linkedin.com/in/sameeksha-aithal/) - aitha010@umn.edu

[Sampada Sathe](https://www.linkedin.com/in/sampada-sathe/) - sathe189@umn.edu
