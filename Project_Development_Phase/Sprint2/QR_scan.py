import cv2
import numpy as np 
import time
import pyzbar.pyzbar as pyzbar 
from ibmcloudant.cloudant_v1 import CloudantV1 
from ibmcloudant import CouchDbSessionAuthenticator 
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator


authenticator = BasicAuthenticator ('apikey-v2-1g0tajj2ya23rva420ga3xjhedsh135ljftxzxvqfxwq', '82bca5b0a21ab96b35d79d5651c15947')
service = CloudantV1(authenticator=authenticator)
service.set_service_url ('https://apikey-v2-ov74n9aiwfps4zcm0ej219bkk2qu7ar613syud6asuc:a48702de86e76254a5d73faa0f667039@8bdd9d2e-653d-460c-95cb-e02b5803b7ca-bluemix.cloudantnosqldb.appdomain.cloud')

cap= cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
	_, frame = cap.read ()
	decodedObjects = pyzbar. decode (frame)
	for obj in decodedObjects:
		#print ("Data", obj.data) 
		a=obj.data.decode('UTF-8') 
		cv2.putText(frame,"Ticket", (50, 50), font, 2,(255,0, 0), 3)
		#print (a)
		try:
			response = service.get_document(db= 'booking', doc_id = a).get_result()
			print(response)
			time.sleep (5)
		except Exception as e:
			print ("Not a Valid Ticket")
			time.sleep (5)
	cv2.imshow ("Frame", frame)
	if cv2.waitKey (1) & 0xFF == ord ('q'):
		break

cap.release ()
cv2.destroyAllWindows ()
client.disconnect ()