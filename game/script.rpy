# Declaration des personnages
define Eiko = Character('Eiko', color="#85E7FF")

# Variables de suivi des projets visites
default visited_iscr = False
default visited_robotique = False
default visited_astronomy = False
default visited_dessin = False

# Declaration des images
image bg classroom = "classroom.jpg"
image bg beach = "beach.jpg"
image bg draw = "draw.jpg"
image bg office = "office.jpg"
image bg ISCR = "ISCR.jpg"
image eiko normal = "eiko.png"
image eiko eyesclosed = "eiko_eyescloses.png"
image eiko enjoy = "eiko_enjoy.png"
image eiko zoom = "eiko_zoom.png"
image eiko shocked = "eiko_shocked.png"
image telescope = "telescope.png"


# Definition de positions personnalisees
transform pos_telescope:
    xpos 500
    ypos 200

transform pos_eiko:
    xpos 700
    ypos 100

# --- CARTE DE CONTACT INTERACTIVE EN PYTHON
screen contact_card():
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 30
        background Solid("#1b2838ee") 
        
        vbox:
            spacing 15
            align (0.5, 0.5)
            
            text "Contact & Profile Summary" size 30 color "#85E7FF" xalign 0.5 bold True
            null height 10
            
            text "Email : Bettypajon1@gmail.com" size 22 color "#ffffff"
            text "LinkedIn : linkedin.com/in/betty-pajon-158299366/" size 22 color "#ffffff"
            text "GitHub : github.com/Eiko-fr" size 22 color "#ffffff"

            null height 20
            textbutton "Close Card":
                xalign 0.5
                action Hide("contact_card")
                

label start:
    
    play music "audio/easy_lemon.ogg" fadein 2.0                
    
    # Afficher l'arriere-plan (decor)
    scene bg classroom
    "In the classroom..."

    # Afficher le personnage Eiko
    show eiko normal
    Eiko "Hi! Nice to meet you."
    
    show eiko eyesclosed
    Eiko "I created a visual novel to learn the basics of Python and introduce myself."
    
    show eiko normal
    Eiko "I am currently a student pursuing a Higher Technician Certificate (BTS) in Technical Engineering Support."
    
    show eiko enjoy
    Eiko "After that, I would like to pursue my engineering studies through a work-study program."
    
    show eiko zoom
    Eiko "Are you looking for work-study students?"
    
    show eiko normal
    Eiko "..."
    
# Debut de la boucle de choix
label question_alternance:
    
    menu:
        "Yes!":
            show eiko enjoy
            Eiko "A very good choice! I would be delighted to join your team."

        "No":
            show eiko eyesclosed
            Eiko "Hmm... Are you sure about that? Try again!"
            jump question_alternance
    
    show eiko zoom
    Eiko "If you wish, you can explore my various passions and projects."

label question_continuer:
    
    menu:
        "YES":
            show eiko enjoy
            Eiko "Very well, thank you for continuing. What would you like to explore first?"

        "No" :
            show eiko normal
            Eiko "....."
            Eiko "Retry"
            jump question_continuer

# --- MENU INTERACTIF DE PRESENTATION ---
label menu_passions:
    
    scene bg classroom
    show eiko normal

    # Verification automatique si tous les projets sont visites
    if visited_iscr and visited_robotique and visited_astronomy and visited_dessin:
        jump scene_conclusion

    menu:
        "ISCR Project" if not visited_iscr:
            jump scene_iscr

        "ISCR Project (Visited)" if visited_iscr:
            jump scene_iscr

        " Robotic Arm Project" if not visited_robotique:
            jump scene_robotique

        "Robotic Arm Project (Visited)" if visited_robotique:
            jump scene_robotique

        "Astronomy" if not visited_astronomy:
            jump scene_astronomy

        "Astronomy (Visited)" if visited_astronomy:
            jump scene_astronomy

        "Drawing & Graphic Design" if not visited_dessin:
            jump scene_dessin

        "Drawing & Graphic Design (Visited)" if visited_dessin:
            jump scene_dessin

# --- SECTION ISCR ---
label scene_iscr:
    $ visited_iscr = True
    scene bg ISCR
    show eiko normal at right 
    Eiko "I am currently working on a project related to my studies for the Institute of Chemical Sciences of Rennes (ISCR)."
    Eiko "The goal is to design a remote monitoring system for gas pressure regulators to facilitate their tracking."
    
    show eiko enjoy
    Eiko "It's still under consideration, but my goal would be to integrate an ESP-32 camera directly onto the pressure gauge, along with an automated alert system and a dedicated web interface."
   
    # --- MINI-QUIZ TECHNIQUE ---
    play music "audio/crossing_the_chasm.ogg" fadein 1.5
    show eiko normal
    Eiko "annnnnd..... now small quiiiiz : why did I choose an ESP32-CAM for this specific embedded IoT setup?"
    
    menu:
        "Because it includes built-in Wi-Fi, Bluetooth, and a cheap camera module for low cost.":
            show eiko enjoy
            Eiko "Spot on! It offers the perfect balance between wireless connectivity, video streaming capabilities, and a low budget for an industrial prototype."

        "Because it has a high-performance desktop-class processor.":
            show eiko eyesclosed
            Eiko "Not quite! It's a low-power microcontroller (Xtensa dual-core), not a heavy desktop CPU, which makes it ideal for edge computing."

        "Because it runs a full Windows operating system.":
            show eiko shocked
            Eiko "Haha, definitely not! It runs on FreeRTOS/MicroPython, way too lightweight for Windows, but perfect for embedded C/C++."

    play music "audio/easy_lemon.ogg" fadein 2
    show eiko normal
    Eiko "It is an ongoing project, but it gives me great hands-on experience in IoT, networking, and embedded systems."
    
    jump menu_passions
    
    
    jump menu_passions

# --- SECTION ROBOTIQUE ---
label scene_robotique:
    $ visited_robotique = True
    scene bg office
    show eiko normal
    Eiko "On a personal level, I am converting an old 3D printer into a functional robotic arm."
    Eiko "I am currently in the 3D design and modeling phase using FreeCAD."
    show eiko enjoy
    Eiko "Don't tell my mechanics professor.. ,  but I vastly prefer FreeCAD to SolidWorks~don't you?"
    show eiko normal
    Eiko "I also had the opportunity to take part in the VAL Robot Challenge, in collaboration with Staubli; we represented our institution and finished second in the rankings ,it was a great experience."
    
    jump menu_passions

# --- SECTION ASTRONOMIE (PLAGE) ---
label scene_astronomy:
    $ visited_astronomy = True
    scene bg beach
    show telescope at pos_telescope
    show eiko normal at pos_eiko

    Eiko "Welcome under the night sky!"
    Eiko "Here is a video of the eclipse captured by the Seestar S50 telescope; there were a lot of clouds that day, so I created a time-lapse video."                       

    hide telescope
    hide eiko
    scene black
    
    stop music fadeout 1.0

    $ renpy.movie_cutscene("images/eclipse.webm")

    play music "audio/easy_lemon.ogg" fadein 1.5
    
    scene bg beach
    show telescope at pos_telescope
    show eiko eyesclosed at pos_eiko
    
    Eiko "I love this quote by Friedrich Nietzsche : As long as you view the stars as something above you, you lack the gaze of one who seeks knowledge."
    
    jump menu_passions

# --- SECTION DESSIN ---
label scene_dessin:
    $ visited_dessin = True
    scene bg draw
    show eiko normal 
    Eiko "I studied graphic design in the past; drawing and creativity will always remain a great pastime for me."
    
    Eiko "In fact, I drew all the character sprites for Eiko used in this Visual Novel!"
    
    hide eiko
    show eiko shocked at center onlayer screens zorder 100
    Eiko "...Wait, can you even read this? ..............................Whooooops I'm blocking the text!"
    
    hide eiko shocked onlayer screens
    show eiko normal
    Eiko "Sorry about that! It allows me to combine technical precision with visual creativity and UI/UX design."
    
    jump menu_passions

# --- SCENE DE CONCLUSION AUTOMATIQUE ---
label scene_conclusion:
    play music "audio/evening.ogg" fadein 2.0
    scene bg classroom
    show eiko enjoy
    
    Eiko "Awesome! You have explored all my projects and passions."
    show eiko normal
    Eiko "Thank you very much for taking the time to discover my work!"
    Eiko "I am highly motivated to bring my engineering skills, creativity, and technical curiosity to your team for a work-study position."
    
    # Affichage de la carte de contact
    Eiko "Here is my contact card:"
    show screen contact_card
    
    show eiko eyesclosed
    Eiko "Feel free to click on the button"
    
    hide screen contact_card
    
    scene black with fade
    

    centered "{size=60}{b}THE END{/b}{/size}\n\n{size=24}Thank you for watching!{/size}\n\n\n{size=14}{color=#888888}Music: \"Evening\" / \"Easy Lemon\" / \"crossing_the_chasm\" by Kevin MacLeod (incompetech.com)\nLicensed under Creative Commons: By Attribution 4.0 License\nhttp://creativecommons.org/licenses/by/4.0/{/color}{/size}"
    
    return
    
