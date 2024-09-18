#########  importing  #########

import pytesseract as pyt
import cv2

#########  Boolean initial value  #########

a = True
b = True

#########  File  #########

while a == True :
    b = True
    
    ## File information ##
    file_name = input("Please enter file name : ")
    extension = input("Please select a file extension (png or jpg) : ")

    ## Check the file extension ##
    if extension == "png" :

        ## Open the file ##
        try :
            image = cv2.imread(f"{file_name}.png")
            pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            text = pyt.image_to_string(gray_image, lang = 'eng')

            ## Result ##
            print(f"\nresult :\n{text}")

            ## Show image ##
            cv2.imshow("Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        except FileNotFoundError:
            print("File not found !\nTry again")
            a = True
            b = False
        except :
            print ("File not found !\nTry again")
            a = True
            b = False
        

        ## Do it again ##
        while b == True :
            again = input("do you want to do it again ? (y/n) ")
            if again == "y" :
                print ("OK")
                a = True
                b = False
            elif again == "n" :
                print ("OK")
                a = False
                b = False
            else :
                print ("I didn't understand what you mean\nTry again")
                b = True

    ## Check the file extension ##
    elif extension == "jpg" :

        ## Open the file ##
        try :
            image = cv2.imread(f"{file_name}.jpg")

            pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            text = pyt.image_to_string(gray_image, lang = 'eng')
            
            ## Result ##
            print(f"\nresult :\n{text}")
        
            ## Show image ##
            cv2.imshow("Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


        except FileNotFoundError:
            print("File not found !\nTry again")
            a = True
            b = False
        except :
            print ("it's wrong")
            a = True
            b = False

        ## Do it again ##
        while b == True :
            again = input("do you want to do it again ? (y/n) ")
            if again == "y" :
                print ("OK")
                a = True
                b = False
            elif again == "n" :
                print ("OK")
                a = False
                b = False
            else :
                print ("I didn't understand what you mean\nTry again")
                b = True

    ## Check the file extension ##
    else :
        print ("It's not defined !\nChoose one of the two extensions jpg or png")
        a = True

end = input(" ")
