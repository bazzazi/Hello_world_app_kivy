###############          ##########        #######   #######        #########      #######       #
#              #        #          #             #         #       #         #           #
#               #       #          #            #         #        #         #          #        #
#              #        #          #           #         #         #         #         #         #
###############         ############          #         #          ###########        #          #
#              #        #          #         #         #           #         #       #           #
#               #       #          #        #         #            #         #      #            #
#              #        #          #       #         #             #         #     #             #
###############         #          #      #######    #######       #         #    #######        #

# Developer: Mohammad Ali Bazzazi (me)

########################### START ###########################
# Importing Libraries
from kivy.app import App 
from kivy.uix.label import Label 

# Create main App class
class MyApp(App): 
    def build(self): 
        # Put a Label in app 
        return Label(text="Hello World", font_size=32) 

# Create instances
if __name__ == "__main__": 
    MyApp().run()
########################### END ###########################
