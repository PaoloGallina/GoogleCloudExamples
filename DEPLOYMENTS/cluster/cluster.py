 
def GenerateConfig(context):
 
  resources = [
	{
      'name': "paolinopaperino",
	  'type': 'container.v1.cluster',
	  'properties': {
			'zone': context.properties['zone'],
			'cluster' : {
				"name": "nuova",
				"initialClusterVersion": context.properties['initial_cluster_version'],
				"description": "Arcus Video Core GKE cluster",
				"network": "default",
				"subnetwork":  "default",
				#"locations": context.properties['locations'],
				"zone": context.properties['zone'],
				"nodePools": [
                    {
						"name": "nodepool-01",
						"config": {
							'imageType': 'cos',
							'machine_type': context.properties['machine_type_standard'],
							'diskSizeGb':  context.properties['machine_disk_size'],
                                                        #'oauthScopes': context.properties['scopes'],
						},
						"initialNodeCount": context.properties['initial_node_count'],
					},
				]
			},
	   },
  	}
  ]
  return {'resources': resources}
 
 
