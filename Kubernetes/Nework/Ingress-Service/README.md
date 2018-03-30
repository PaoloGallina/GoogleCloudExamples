Example of ingress redirecting to two diffrent services (apache and nginx) basing the choice on the path
`http://ip/apache`
`http://ip/nginx`

    kubectl run httpd --image=httpd:2.4
    kubectl run nginx --image=nginx
    kubectl create -f ingress&service.yaml 
