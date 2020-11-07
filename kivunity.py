#! /usr/bin/python

import re
import sys
import os 
from android.runnable import run_on_ui_thread
from jnius import autoclass, PythonJavaClass, java_method, cast
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import logging

testmode = True
#inter_id = "12839"
#app_id = "3786901"
inter_id = 0
app_id = 0

PythonActivity = autoclass("org.kivy.android.PythonActivity")
Unity_ads_listener = autoclass("com.unity3d.ads.IUnityAdsListener")
Unity_ads = autoclass("com.unity3d.ads.UnityAds")
logging.warning("\n\n You've reached passed init \n\n")



              

class Unity_handler():
    

   def __init__(self, app_id_2):
     self.a_id = app_id_2
   
   def init_unity(self):
     global app_id
     app_id = self.a_id  
     self.new_ad_listener = UnityAdsListener()
     #Unity_ads.addListener(new_ad_listener)
     Unity_ads.setListener(self.new_ad_listener)
     self.c_activity = cast('android.app.Activity',PythonActivity.mActivity)
     Unity_ads.initialize(self.c_activity,app_id,testmode)
     #Unity_ads.initialize(PythonActivity.mActivity,app_id,testmode)
       
 
   def show_ad(self, id_num):
     global inter_id   
     #show interstial ads
     inter_id = id_num
     logging.warning("\n\n self.c_activity="+str(self.c_activity)+"\n\n")
     logging.warning("\n\n app_id="+str(app_id)+"\n\n")
     logging.warning("\n\n new_ad_listener="+str(self.new_ad_listener)+"\n\n")

     if Unity_ads.isReady(inter_id):
          try:
            Unity_ads.show(self.c_activity, inter_id)
            
          except:
            logging.warning("Unity ads not ready and thus has not been loaded") 

 
class UnityAdsListener(PythonJavaClass):
    __javainterfaces__= ['com/unity3d/ads/IUnityAdsListener']
    __javacontext__= 'app'

    @java_method('(Ljava/lang/String;)V')
    def onUnityAdsReady(self,inter_id):
       logging.warning("\n\n ADS are ready! "+ str(inter_id) + " \n\n")
       #pass        

    @java_method('(Ljava/lang/String;)V')   
    def onUnityAdsStart(self,inter_id):
       #pass
       logging.warning("\n\n ADS are starting! " + self(inter_id) + "\n\n")

    @java_method('(Ljava/lang/String;Lcom/unity3d/ads/UnityAds$FinishState;)V')
    def onUnityAdsFinish(self,inter_id,finish_state):
       #pass
       logging.warning("\n\n ADS are FINISHED! "+str(finish_state) + " \n\n")
       #appl_id = u_h.app_id2                                                     

 
    @java_method('(Lcom/unity3d/ads/UnityAds$UnityAdsError;Ljava/lang/String;)V')
    def onUnityAdsError(self,error, message):
       #pass 
       logging.warning("\n\n ADS are in error! \n\n")


