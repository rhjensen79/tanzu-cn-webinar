
.PHONY: setup create_cluster_pre delete_cluster_pre	login_cluster demo_app

test: 
	@ direnv allow .
	@ wait $!
	kubectl vsphere login --server=${wcp} --insecure-skip-tls-verify -u=${KUBECTL_VSPHERE_USER}

setup: 
	@ direnv allow .
	@ wait $!
	kubectl vsphere login --server=${wcp} --insecure-skip-tls-verify -u=${KUBECTL_VSPHERE_USER}
	kubectl config use-context ${KUBECTL_CONTEXT}

create_cluster_pre: setup
	kubectl apply -f pre-k8s.yaml -n ${KUBECTL_CONTEXT}

delete_cluster_pre: setup
	kubectl delete -f pre-k8s.yaml -n ${KUBECTL_CONTEXT} --wait=false

login_cluster_pre:
	direnv allow .
	kubectl vsphere login --server=${wcp} --insecure-skip-tls-verify -u=${KUBECTL_VSPHERE_USER} --tanzu-kubernetes-cluster-name pre-k8s --tanzu-kubernetes-cluster-namespace ${KUBECTL_CONTEXT}

create_cluster: setup
	kubectl apply -f demo-cluster.yaml -n ${KUBECTL_CONTEXT}

delete_cluster: setup
	kubectl delete -f demo-cluster.yaml -n ${KUBECTL_CONTEXT} --wait=false