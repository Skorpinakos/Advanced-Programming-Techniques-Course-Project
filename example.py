import videocensor

location='api_controller.py' #give the location of the service directory for example C:\Users\ioannis\Desktop\VS CODE\tran_4\Advanced_Programming_Techniques_2022-main\api_controller.py 
Censorer=videocensor.initialize(location,storage_mode='RAM') #create an instance of the tool
result=Censorer.censor('directory/test.mp4',[],[]) #use the tool on a local video
print(result.info) #print return data
with open('edited_video.mp4','wb') as file:
    file.write(result.video) #save the returned video as file
