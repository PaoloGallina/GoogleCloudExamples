I have implemented the scaling:
-

- with the metrics retrieved from a pod not belonging to the deployment "SameDeployment.yaml", 
- with metrics coming from the very same deployment "DifferentDeploymentFromPod.yaml" 

To replicate you have to enable the cluster to retrieve the custom metrics 

    `kubectl create -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-stackdriver/master/custom-metrics-stackdriver-adapter/adapter-beta.yaml `

Kubernetes Examples
https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/
