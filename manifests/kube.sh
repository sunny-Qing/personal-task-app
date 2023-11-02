kubectl apply -f mongo-pv.yaml
kubectl apply -f mongo.yaml
kubectl apply -f profileapp.yaml
kubectl apply -f tasksapp.yaml

kubectl apply -f profileconfig.yaml
# Extract the clusterIP
export profileip=$( kubectl get services/profileapp-svc --template='{{.spec.clusterIP}}' )
# Retrieve the ConfigMap, replace "NOTSET" with the clusterIP, and re-apply.
kubectl get configmap/profile-config -o yaml | sed -r "s/NOTSET/$profileip/" | kubectl apply -f -


kubectl apply -f taskconfig.yaml
# Extract the clusterIP
export taskip=$( kubectl get services/tasksapp-svc --template='{{.spec.clusterIP}}' )
# Retrieve the ConfigMap, replace "NOTSET" with the clusterIP, and re-apply.
kubectl get configmap/task-config -o yaml | sed -r "s/NOTSET/$taskip/" | kubectl apply -f -


# Finally, start the gateway
kubectl apply -f gateway.yaml
