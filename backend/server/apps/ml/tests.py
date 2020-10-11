from django.test import TestCase
import inspect
from apps.ml.registry import MLRegistry

from apps.ml.ddos_classifier.random_forest import RandomForestClassifier

class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {
	    	'Destination_Port': 80.0, 
		'Flow_Duration': 3.0, 
		'Total_Fwd_Packets': 2.0, 
		'Total_Backward_Packets': 1.0, 
		'Total_Length_of_Fwd_Packets': 0.0, 
		'Total_Length_of_Bwd_Packets': 0.0, 
		'Fwd_Packet_Length_Max': 168.0, 
		'Fwd_Packet_Length_Min': 0.0, 
		'Fwd_Packet_Length_Mean': 0.0, 
		'Fwd_Packet_Length_Std': 0.0, 
		'Bwd_Packet_Length_Max': 0.0, 
		'Bwd_Packet_Length_Min': 0.0, 
		'Bwd_Packet_Length_Mean': 0.0, 
		'Bwd_Packet_Length_Std': 0.0, 
		'Flow_Bytes_Sec': 0.0, 
		'Flow_Packets_Sec': 219948.0, 
		'Flow_IAT_Mean': 3.0,
		'Flow_IAT_Std': 0.0, 
		'Flow_IAT_Max': 3.0, 
		'Flow_IAT_Min': 3.0, 
		'Fwd_IAT_Total': 0.0, 
		'Fwd_IAT_Mean': 0.0, 
		'Fwd_IAT_Std': 0.0, 
		'Fwd_IAT_Max': 0.0, 
		'Fwd_IAT_Min': 3.0, 
		'Bwd_IAT_Total': 0.0, 
		'Bwd_IAT_Mean': 0.0, 
		'Bwd_IAT_Std': 0.0, 
		'Bwd_IAT_Max': 0.0, 
		'Bwd_IAT_Min': 0.0, 
		'Fwd_PSH_Flags': 0.0, 
		'Bwd_PSH_Flags': 0.0, 
		'Fwd_URG_Flags': 0.0, 
		'Bwd_URG_Flags': 0.0, 
		'Fwd_Header_Length': 40.0, 
		'Bwd_Header_Length': 40.0, 
		'Fwd_Packets_Sec': 666666.6667, 
		'Bwd_Packets_Sec': 0.0, 
		'Min_Packet_Length': 0.0, 
		'Max_Packet_Length': 168.0, 
		'Packet_Length_Mean': 0.0, 
		'Packet_Length_Std': 0.0, 
		'Packet_Length_Variance': 0.0, 
		'FIN_Flag_Count': 0.0, 
		'SYN_Flag_Count': 0.0, 
		'RST_Flag_Count': 0.0, 
		'PSH_Flag_Count': 0.0, 
		'ACK_Flag_Count': 0.0, 
		'URG_Flag_Count': 0.0, 
		'CWE_Flag_Count': 0.0, 
		'ECE_Flag_Count': 0.0, 
		'Down_Up_Ratio': 0.0, 
		'Average_Packet_Size': 0.0, 
		'Avg_Fwd_Segment_Size': 0.0, 
		'Avg_Bwd_Segment_Size': 0.0, 
		'Fwd_Avg_Bytes_Bulk': 0.0, 
		'Fwd_Avg_Packets_Bulk': 0.0, 
		'Fwd_Avg_Bulk_Rate': 0.0, 
		'Bwd_Avg_Bytes_Bulk': 0.0, 
		'Bwd_Avg_Packets_Bulk': 0.0, 
		'Bwd_Avg_Bulk_Rate': 0.0, 
		'Subflow_Fwd_Packets': 2.0, 
		'Subflow_Fwd_Bytes': 0.0, 	
		'Subflow_Bwd_Packets': 1.0, 
		'Subflow_Bwd_Bytes': 0.0, 
		'Init_Win_bytes_forward': -1.0, 
		'Init_Win_bytes_backward': 29200.0, 
		'act_data_pkt_fwd': 1.0, 
		'min_seg_size_forward': 0.0, 
		'Active_Mean': 0.0, 'Active_Std': 0.0, 
		'Active_Max': 0.0, 'Active_Min': 0.0, 
		'Idle_Mean': 0.0, 
		'Idle_Std': 0.0, 
		'Idle_Max': 0.0, 
		'Idle_Min': 0.0
            
        }
        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('BENING', response['label'])
    def test_registry(self):
            registry = MLRegistry()
            self.assertEqual(len(registry.endpoints), 0)
            endpoint_name = "ddos_classifier"
            algorithm_object = RandomForestClassifier()
            algorithm_name = "random forest"
            algorithm_status = "production"
            algorithm_version = "0.0.1"
            algorithm_owner = "Mark Silla"
            algorithm_description = "Random Forest with simple pre- and post-processing"
            algorithm_code = inspect.getsource(RandomForestClassifier)
            # add to registry
            registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                        algorithm_status, algorithm_version, algorithm_owner,
                        algorithm_description, algorithm_code)
            # there should be one endpoint available
            self.assertEqual(len(registry.endpoints), 1)
