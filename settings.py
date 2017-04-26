#settings.py


'''
settings = {"min_subgroup_length": 3, "max_subgroup_length": 6, "subgroup_length": 3, # general
			"lincorr_lag": 5, # candidate generation
			"VARMA_p": 2, "VARMA_q": 0, "ARMA_q": 2, # VARMA orders
			"re_series": np.logspace(-1,-6,num_series), "rw_series": 500*np.logspace(0,-1,num_series), # VARMA training
			"num_timepoints": 1000, "num_samples": 10, "case": "case1", # VARMA sim
			"train_share": 0.4, "test_share": 0.4, # splitting
			"failure_horizon": 20, "pos_w": 1.5, # classification and regression
			#"A_architecture": "DLR", "B_architecture": "SECTIONS", "C_architecture": "SELECTED", "f_architecture": "TANH", # ESN
			#"ESN_size_state": 500, 
			"ESN_spec": [("RODAN", {"N": 500,"v":0}),
						("RODAN",{"N":500,"v":1}),
						("VAR", {"p": 20}),
						("THRES", {"N": 200,"random_thres":True,"direct_input":True}),
						#("TRIGGER", {"N": 500,"random_thres": True,"direct_input":True}),
						#("LEAKY", {"N": 200, "r": 0.8,"v":1}),
						#("HEIGHTSENS", {"N": 200, "random_thres": True}),
						("DIRECT",None),
						],
			"ESN_size_out": 20, # ESN
			"ESN_burn_in": 10,"ESN_batch_train" : True,"ESN_tikhonov_const": 10,  # ESN training
			"ESN_sim_case": "trigger_waves", # ESN sim
			"ESN_mixing": [("TRIGGER","RODAN",200), ("THRES","RODAN",200), ("RODAN","TRIGGER",200), ("RODAN","THRES",100),
						   ("THRES","VAR",1), ("VAR","TRIGGER",1), ("LEAKY","TRIGGER",20), ("THRES","LEAKY",50), ("LEAKY","RODAN",100),
						   ("HEIGHTSENS","HEIGHTSENS",1),("HEIGHTSENS","LEAKY",200),("RODAN","HEIGHTSENS",200),
						   ("VAR","RODAN",10),("RODAN","RODAN",100)],
			"ESN_rebuild_types": ["THRES","TRIGGER"], "ESN_rebuild_iterations": 1, "ESN_impact_limit": 1e-2,
			"ESN_classifier": "LINEAR", "ESN_sig_limit": 1.1
			}
'''

dodgers = {"train_share": 0.4, "test_share": 0.4, # splitting
			"pos_w": 1.5, # classification and regression
			"ESN_spec": [#("RODAN", {"N": 500,"v":0}),
						("RODAN",{"N":500,"v":1}),
						("VAR", {"p": 20}),
						("THRES", {"N": 200,"random_thres":True,"direct_input":True}),
						#("TRIGGER", {"N": 500,"random_thres": True,"direct_input":True}),
						("LEAKY", {"N": 200, "r": 0.9,"v":1}),
						#("HEIGHTSENS", {"N": 200, "random_thres": True}),
						#("DIRECT",None),
						],
			"ESN_size_out": 20, # ESN
			"ESN_burn_in": 10,"ESN_batch_train" : True,"ESN_tikhonov_const": 3,  # ESN training
			"ESN_sim_case": "trigger_waves", # ESN sim
			"ESN_mixing": [("LEAKY","THRES",100),("THRES","RODAN",200),("VAR","THRES",20)],
			"ESN_rebuild_types": ["THRES","TRIGGER"], "ESN_rebuild_iterations": 1, "ESN_impact_limit": 1e-2,
			"ESN_classifier": "SVM", "ESN_sig_limit": 0.9
			}

occupancy = {"train_share": 0.4, "test_share": 0.4, # splitting
			"pos_w": 1, # classification and regression
			"ESN_spec": [#("RODAN", {"N": 500,"v":0}),
						("RODAN",{"N":500,"v":1}),
						("VAR", {"p": 10}),
						("THRES", {"N": 200,"random_thres":True,"direct_input":True}),
						#("TRIGGER", {"N": 500,"random_thres": True,"direct_input":True}),
						("LEAKY", {"N": 200, "r": 0.8,"v":1}),
						#("HEIGHTSENS", {"N": 200, "random_thres": True}),
						("DIRECT",None),
						],
			"ESN_size_out": 20, # ESN
			"ESN_burn_in": 10,"ESN_batch_train" : True,"ESN_tikhonov_const": 10,  # ESN training
			"ESN_sim_case": "trigger_waves", # ESN sim
			"ESN_mixing": [],
			"ESN_rebuild_types": ["THRES","TRIGGER"], "ESN_rebuild_iterations": 1, "ESN_impact_limit": 1e-2,
			"ESN_classifier": "LINEAR", "ESN_sig_limit": 1.1
			}

settings = {"DODGERS": dodgers, "OCCUPANCY": occupancy}