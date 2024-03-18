import sys
import pygame
import random

LIGHT_GREEN = (144, 238, 144)
DARK_GREEN = (0, 100, 0)
ORANGE = (255, 140, 0)
# DARK_PINK = (255, 190, 193)
# DARK_PINK = (239,53,170)
# DARK_PINK = (255, 105, 180)
DARK_PINK = (246, 125, 146)
colors = ['blue', 'green', ORANGE, 'purple', 'red', 'yellow']

def create_code(colors, number, repeat):
    """Deze functie genereert de kleurcode die geraden moet worden. 
    Input-variabelen: 
    - number (= aantal kleuren in de code) 
    - repeat (Boolse variabele: geeft aan of een kleur vaker in de code mag voorkomen)
    De functie retourneert een code"""

    code = []
    colors_copy = colors[:]
                       
    for i in range(number):
        # print('colors = ' + str(colors))
        # print('Lengte colors:' + str(len(colors)))
        index = random.randint(0, len(colors_copy)-1) 
        # print('Willekeurig gekozen index: ' + str(index))
        color = colors_copy[index]
        # print('Gekozen kleur: ' + color)
        code.append(color)
        # print('code: ' + str(code))
        
        if repeat == 'no':
            colors_copy.pop(index)

    return code

def check_code(code, guess):
    """Deze functie vergelijkt de invoer van de gebruiker met de gegenereerde code.
    Input-variabelen:
    - code: de code die via de functie create_code is gegenereerd
    - guess: de gok van de gebruiker
    Deze functie retourneert: 
    - aantal juiste kleur op juiste plek
    - aantal juiste kleur op verkeerde plek
    """
    correct_place_color = 0
    correct_color = 0
    code_checked = [False] * len(code)
    guess_checked = [False] * len(guess)

    # Eerst controleren we voor correcte kleuren op de juiste plaats
    for index in range(len(code)):
        if code[index] == guess[index]:
            correct_place_color += 1
            # Markeer deze posities als gecontroleerd
            code_checked[index] = True
            guess_checked[index] = True

    # Nu controleren we voor correcte kleuren op de verkeerde plaats
    for index, guess_color in enumerate(guess):
        if not guess_checked[index]:
            for code_index, code_color in enumerate(code):
                if not code_checked[code_index] and guess_color == code_color:
                    correct_color += 1
                    # Markeer deze posities als gecontroleerd
                    code_checked[code_index] = True
                    guess_checked[index] = True
                    break

    return correct_color, correct_place_color

def feedback_guess(correct_color, correct_place_color):
    """Deze functie geeft aan de gebruiker feedback naar aanleiding van zijn gok"""
    # print('Aantal juiste kleur en op juiste plek: ' + str(correct_place_color))
    # print('Aantal juiste kleur, maar niet op juiste plek: ' + str(correct_color))

def create_guess_circles_dict(screen, centers_list, color_dict, radius):
    """ Deze functie retourneert een woordenboek met daarin alle cirkels waarin de gebruiker zijn gok kan invoeren.
        De keys zijn de nummers van de cirkels, de values, de cirkel
    """
    guess_circles_dict = {}

    for i in range(len(centers_list)):
        guess_circles_dict[i] = pygame.draw.circle(screen, color_dict[i], centers_list[i], radius)
    
    return guess_circles_dict

def generate_centers_list(number_rows, number_columns, radius):
    """Deze functie genereert een lijst van de coordinaten van de middelpunten van alle cirkels"""
    centers_list = []
    for i in range(number_rows):
        y = 100 + 3*radius*i
        for j in range(number_columns):
            x = 100 + 3*radius*j
            centers_list.append((x,y))

    #print(centers_list)
    return centers_list 

def generate_guess_cicle_color_dict(number_rows, number_columns, color):
    total = number_rows * number_columns
    target_color_dict = {}
    for i in range(total):
        target_color_dict[i] = color
    
    return target_color_dict       
       
# centers_list = generate_centers_list(12, 4, 15)
# print(centers_list)

def draw_circles(screen, centers, radius):
    """Deze functie tekent de circkels op het PythonMind bord"""
    for center in centers:
        pygame.draw.circle(screen, (32,32,32), center, radius)

def draw_circle(screen, color, position):
    """deze functie tekent een cirkel met de gegeven coordinaten"""
    circle = pygame.draw.circle(screen, color, position, 15)
    
    return circle

def generate_check_centers_list(number_rows):
    """Deze functie retourneert op basis van het aantal rijen een lijst met alle centra van de cirkels waari Pythonmind de gebruiker feedback geeft op zijn poging"""
    check_centers_list = []
    for i in range(number_rows):
        check_centers_list.append((277, 89 + i* 45))
        check_centers_list.append((297, 89 + i* 45))
        check_centers_list.append((277, 109 + i* 45))
        check_centers_list.append(((297, 109 + i* 45)))

    return check_centers_list

def generate_check_cicle_color_dict(number_rows, number_columns, color):
    total = number_rows * number_columns
    check_color_dict = {}
    for i in range(total):
        check_color_dict[i] = color
    
    return check_color_dict   

def create_check_circles_dict(screen, centers_list, color_dict, radius):
    """ Deze functie retourneert een woordenboek met daarin alle cirkels waarin de gebruiker zijn gok kan invoeren.
        De keys zijn de nummers van de cirkels, de values, de cirkel
    """
    check_circles_dict = {}

    for i in range(len(centers_list)):
        check_circles_dict[i] = pygame.draw.circle(screen, color_dict[i], centers_list[i], radius)
    
    return check_circles_dict



def draw_check_circles(screen, number_rows, radius):
    """Deze functie tekent de circels waar later de feedback wordt getoond"""
    dict_check_circles = {}
    for i in range(number_rows):
        row_num = str(i)

        dict_check_circles[str(row_num + '_check_1')] = pygame.draw.circle(screen,(32,32,32), (277, 89 + i* 45), radius)
        dict_check_circles[str(row_num + '_check_2')] = pygame.draw.circle(screen,(32,32,32), (297, 89 + i* 45), radius)
        dict_check_circles[str(row_num + '_check_3')] = pygame.draw.circle(screen,(32,32,32), (277, 109 + i* 45), radius)
        dict_check_circles[str(row_num + '_check_4')] = pygame.draw.circle(screen,(32,32,32), (297, 109 + i* 45), radius) 

    return dict_check_circles 

def generate_feedback_list(turn, num_rows, num_cols):
    """Deze functie neemt als invoer-variabelen de beurt, het aantal rijen en aantal kolommen 
    en retourneert een lijst waarin de nummers van de cirkels staan waarin een kleur geplaatst mag worden"""
    feedback_positions = []
    for i in range(0,4):
        position = num_cols*(num_rows + 1 - turn) - (i+1)
        feedback_positions.append(position)
    feedback_positions.sort()
    # print('Toegestande positie voor beurt ' + str(turn) + ':')
    # print(allowed_guess_positions)
    
    return feedback_positions

def generate_feedback_colors(num_red, num_white):
    """Deze functie neemt als invoer het aantal juiste kleur en op juiste plek (num_red) en het aantal juiste kleur maar niet op juiste plek (num_white)
     en retourneert een lijst met daarin de kleuren die de check_circles moeten krijgen"""
    feedback_colors = [(32,32,32), (32,32,32), (32,32,32), (32,32,32)]

    # if num_red == 0 and num_white == 0:
    #    feedback_colors = [(45,45,45), (45,45,45), (45,45,45), (45,45,45)]
    
    if num_red > 0:
        for i in range(num_red):
            feedback_colors[i] = 'red'
    if num_white > 0:
        for i in range(num_white):
            feedback_colors[num_red + i] = 'white'
    
    return feedback_colors
    
def show_feedback(feedback_positions, feedback_colors, check_color_dict):
    """Met behulp van deze functie geven we de check_circles de juiste kleuren om de gebruiker feedback te geven"""
    for i in range(len(feedback_positions)):
        check_color_dict[feedback_positions[i]] = feedback_colors[i]

def draw_colors(screen, color_circles, number_colors, radius):
    """Deze functie tekent alle kleuren waar de gebruiker uit kan kiezen"""   
    color_circles_first_row = {}
    color_circles_second_row = {}
    
    if number_colors == 6:  
        color_circles_first_row = {}
        color_circles_second_row = {}  
        color_first_row = ['blue', 'green', ORANGE]
        color_second_row = ['purple', 'red', 'yellow']

        for i, color in enumerate(color_first_row):
            if isinstance(color, str):
                color_circles_first_row[color] = pygame.draw.circle(screen, color, (120+3*i*radius, 670), 15)
            else:
                color_circles_first_row[color] = pygame.draw.circle(screen, color, (120+3*i*radius, 670), 15)
    
        for i, color in enumerate(color_second_row):
            if isinstance(color, str):
                color_circles_second_row[color] = pygame.draw.circle(screen, color, (120+3*i*radius, 715), 15)
            else:
                color_circles_second_row[color] = pygame.draw.circle(screen, color, (120+3*i*radius, 715), 15)  
        
    elif number_colors == 8:
        color_first_row = ['blue', 'green', ORANGE, DARK_PINK]
        color_second_row = ['purple', 'red', 'yellow', 'turquoise']

        for i, color in enumerate(color_first_row):
            if isinstance(color, str):
                color_circles_first_row[color] = pygame.draw.circle(screen, color, (120+3*i*radius, 670), 15)
            else:
                color_circles_first_row[color] = pygame.draw.circle(screen, color, (120+3*i*radius, 670), 15)
    
        for i, color in enumerate(color_second_row):
            if isinstance(color, str):
                color_circles_second_row[color] = pygame.draw.circle(screen, color, (120+3*i*radius, 715), 15)
            else:
                color_circles_second_row[color] = pygame.draw.circle(screen, color, (120+3*i*radius, 715), 15)  
    
    elif number_colors == 10:
        color_first_row = ['blue', 'green', ORANGE, DARK_PINK, 'black']
        color_second_row = ['purple', 'red', 'yellow', 'turquoise', 'white']

        for i, color in enumerate(color_first_row):
            if isinstance(color, str):
                color_circles_first_row[color] = pygame.draw.circle(screen, color, (120+3*i*radius, 670), 15)
            else:
                color_circles_first_row[color] = pygame.draw.circle(screen, color, (120+3*i*radius, 670), 15)
    
        for i, color in enumerate(color_second_row):
            if isinstance(color, str):
                color_circles_second_row[color] = pygame.draw.circle(screen, color, (120+3*i*radius, 715), 15)
            else:
                color_circles_second_row[color] = pygame.draw.circle(screen, color, (120+3*i*radius, 715), 15) 
                
    # Samenvoegen van beide dictionaries
    color_circles = color_circles_first_row.copy()
    color_circles.update(color_circles_second_row)       
    
    return color_circles
    
def draw_horizontal_lines(screen, number_rows):
    "Deze functie tekent de horizontale gele lijnen op het PythonMind bord"
    for i in range(number_rows):
        pygame.draw.line(screen, (255, 255, 153), [70, 77 + i*45], [310, 77 + i*45]) 

def generate_allowed_circles_list(turn, num_rows, num_cols):
    """Deze functie neemt als invoer-variabelen de beurt, het aantal rijen en aantal kolommen 
    en retourneert een lijst waarin de nummers van de cirkels staan waarin een kleur geplaatst mag worden"""
    allowed_guess_positions = []
    for i in range(0,4):
        position = num_cols*(num_rows + 1 - turn) - (i+1)
        allowed_guess_positions.append(position)
    allowed_guess_positions.sort()
    # print('Toegestande positie voor beurt ' + str(turn) + ':')
    # print(allowed_guess_positions)
    
    return allowed_guess_positions

def draw_button(screen, bg_color, left, top, width, height, text, text_color):
    """Deze functie retourneert een knop met 'text' met de gegeven positie en afmetingen"""
    button_rect = pygame.Rect(left, top, width, height)
    button = pygame.draw.rect(screen, bg_color, button_rect)

    font = pygame.font.Font(None, 26)
    text = font.render(text, True, text_color)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

    return button

def show_selected_option(screen, left, top, width, height):
    selected_option = pygame.draw.rect(screen, 'red', pygame.Rect(left, top, width + 3, height + 3),  3)
    
    return selected_option

def reset_game(colors, num_rows, number, repeat):
    """Deze functie reset het spel: dit is dus een manier om opnieuw te kunnen beginnen"""
    # De beurt wordt weer op 1 gezet:
    turn = 1
    # Er wordt een nieuwe code gemaakt
    code = create_code(colors, number, repeat)
    # De kleuren van de guess-circles and check-circles worden weer op de start-kleur gezet
    check_color_dict = generate_check_cicle_color_dict(num_rows, number, (32,32,32))      
    target_color_dict = generate_guess_cicle_color_dict(num_rows, number, (32,32,32))
    # De lijst van cirkels waar de gebruiker zijn poging kan invoeren, wordt weer op de onderste rij gezet
    turn_circles = generate_allowed_circles_list(turn, num_rows, number)

    return turn, code, check_color_dict, target_color_dict, turn_circles
            
def run_game():

    pygame.init()
    screen = pygame.display.set_mode((650, 800))
    pygame.display.set_caption("PythonMind - version 1.0")
    
    # Definitie variabelen:
    orange = (255,140,0)
    chosen_color = None         
    moving = False
    turn = 1

    color_circles = {}
    colors_6 = ['blue', 'green', ORANGE, 'purple', 'red', 'yellow']
    colors_8 = ['blue', 'green', ORANGE, 'purple', 'red', 'yellow', DARK_PINK, 'turquoise']
    colors_10 = ['blue', 'green', ORANGE, 'purple', 'red', 'yellow', DARK_PINK, 'turquoise', 'white', 'black'] 
    
    # Standaardinstellingen:
    colors = colors_6
    repeat_list = ['no']
    number_colors_list = [6]

    code = create_code(colors, 4, repeat_list[-1])
    # print(code)

    turn_circles = generate_allowed_circles_list(turn, 12, 4)
    target_color_dict = generate_guess_cicle_color_dict(12, 4, (32,32,32))
    # print(target_color_dict)

    check_color_dict = generate_check_cicle_color_dict(12, 4, (32,32,32))

    # Weergave van de geselecteerde opties mbt moeilijkheidsgraad: geselecteerde optie heeft een rode rand
    # Default instelingen: 6 kleuren en geen herhaling
    select_color_left = 400
    select_color_top = 300
    select_color_width = 50
    select_color_height = 50

    select_repeat_left = 475
    select_repeat_top = 405
    select_repeat_width = 50
    select_repeat_height = 50      

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #print(mouse_pos)
                for key, value in color_dict.items():
                    if value.collidepoint(mouse_pos):
                        moving = True
                        chosen_color = key 
                        # print(chosen_color)
                        copy_circle = draw_circle(screen, chosen_color, mouse_pos)
                        # print(moving)         
              # Check for the mouse button down event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Call the on_mouse_button_down() function
                if start_button.collidepoint(event.pos):
                    # print("Button clicked!")   
                    turn, code, check_color_dict, target_color_dict, turn_circles = reset_game(colors, 12, 4, repeat_list[-1])
                    # print(turn)
                    # print(code)
                    # print(turn_circles) 
                if color_six.collidepoint(event.pos):
                    select_color_left = color_six.left
                    select_color_top = color_six.top
                    select_color_width = color_six.width
                    select_color_height = color_six.height   
                    
                    colors = colors_6
                    number_colors_list.append(6)
                    code = create_code(colors, 4, repeat_list[-1])

                    #print(code)

                    turn, code, check_color_dict, target_color_dict, turn_circles = reset_game(colors, 12, 4, repeat_list[-1])

                if color_eight.collidepoint(event.pos):
                    select_color_left = color_eight.left
                    select_color_top = color_eight.top
                    select_color_width = color_eight.width
                    select_color_height = color_eight.height
                    
                    colors = colors_8
                    number_colors_list.append(8)
                    code = create_code(colors, 4, repeat_list[-1])

                    #print(code)

                    turn, code, check_color_dict, target_color_dict, turn_circles = reset_game(colors, 12, 4, repeat_list[-1])

                if color_ten.collidepoint(event.pos):
                    select_color_left = color_ten.left
                    select_color_top = color_ten.top
                    select_color_width = color_ten.width
                    select_color_height = color_ten.height

                    colors = colors_10
                    number_colors_list.append(10)
                    code = create_code(colors, 4, repeat_list[-1])

                    #print(code)

                    turn, code, check_color_dict, target_color_dict, turn_circles = reset_game(colors, 12, 4, repeat_list[-1])

                if repeat_yes.collidepoint(event.pos):
                    select_repeat_left = repeat_yes.left
                    select_repeat_top = repeat_yes.top
                    select_repeat_width = repeat_yes.width
                    select_repeat_height = repeat_yes.height

                    repeat_list.append('yes')
                    code = create_code(colors, 4, repeat_list[-1])
                    
                    # print(code)

                    turn, code, check_color_dict, target_color_dict, turn_circles = reset_game(colors, 12, 4, repeat_list[-1])
                
                if repeat_no.collidepoint(event.pos):
                    select_repeat_left = repeat_no.left
                    select_repeat_top = repeat_no.top
                    select_repeat_width = repeat_no.width
                    select_repeat_height = repeat_no.height

                    repeat_list.append('no') 
                    code = create_code(colors, 4, repeat_list[-1]) 

                    # print(code)                    

                    turn, code, check_color_dict, target_color_dict, turn_circles = reset_game(colors, 12, 4, repeat_list[-1])

            elif event.type == pygame.MOUSEMOTION and moving:
                #print(chosen_color)
                mouse_pos = pygame.mouse.get_pos()
                screen.fill((0,0,0))
                pygame.draw.rect(screen, (139,69,19), rect)
                copy_circle = draw_circle(screen, chosen_color, mouse_pos) 

                for key, value in circle_dict.items():                                        
                    if value.collidepoint(mouse_pos) and key in turn_circles:
                        target_id = key
                        target_color_dict[target_id] = chosen_color
                        screen.fill((0,0,0))
                        pygame.draw.rect(screen, (139,69,19), rect)
                        moving = False

            elif event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.rect(screen, (139,69,19), rect)
                # copy_circle = draw_circle(screen, chosen_color, mouse_pos)
                moving = False

        if moving == False:
            screen.fill((0,0,0))


        rect = pygame.Rect(50, 50, 290, 700)
        pygame.draw.rect(screen, (139,69,19), rect)

        check_centers_list = generate_check_centers_list(12)
        check_dict = create_check_circles_dict(screen, check_centers_list, check_color_dict, 8)
        #pygame.draw.circle(screen, (64,64,64), (100,100), 25)
        centers_list = generate_centers_list(12, 4, 15)
        circle_dict = create_guess_circles_dict(screen, centers_list, target_color_dict, 15)

        # checken of de gebruiker een guess heeft gedaan: 
        # dit houdt in dat (32,32,32) niet meer voorkomt als kleur van de vier cirkels die horen bij de beurt
        # Maak lijst van kleuren en check dat (32,32,32) er niet meer in zit
        turn_circle_colors = []
        if turn < 13:
            for circle in turn_circles:
                color = target_color_dict[circle]
                turn_circle_colors.append(color)
            # print(turn_circle_colors)

            if (32,32,32) not in turn_circle_colors:
                correct_color, correct_place_color = check_code(code, turn_circle_colors)
                feedback_guess(correct_color, correct_place_color)
                feedback_list = generate_feedback_list(turn, 12, 4)
                feedback_colors = generate_feedback_colors(correct_place_color, correct_color)
                for i in range(len(feedback_colors)):
                    check_color_dict[feedback_list[i]] = feedback_colors[i]
                
                if correct_place_color != 4:
                    turn += 1
                    # print(turn)
                    turn_circles = generate_allowed_circles_list(turn, 12, 4)
                elif correct_place_color == 4:
                    moving = False
                    score = 13 - turn - 1
                        
        # draw_circles(screen, centers_list, 15)
        pygame.draw.line(screen, (255, 255, 153),[70, 77], [70, 617])
        pygame.draw.line(screen, (255, 255, 153),[265, 77], [265, 617])
        pygame.draw.line(screen, (255, 255, 153),[310, 77], [310, 617]) 

        draw_horizontal_lines(screen, 13) 
        # check_circles = draw_check_circles(screen, 12, 8)
        
        color_dict = draw_colors(screen, color_circles, number_colors_list[-1], 15)
        
        if moving:
            copy_circle = draw_circle(screen, chosen_color, mouse_pos)  

        # Knoppen om spelinstellingen te kiezen: aantal kleuren
        start_button = draw_button(screen, LIGHT_GREEN, 400, 75, 150, 50, 'Nieuw spel', DARK_GREEN)  
        number_colors = draw_button(screen, 'black', 393, 250, 150, 50, 'Aantal Kleuren: ', LIGHT_GREEN) 
        color_six = draw_button(screen, LIGHT_GREEN, 400, 300, 50, 50, '6', DARK_GREEN)   
        color_eight = draw_button(screen, LIGHT_GREEN, 475, 300, 50, 50, '8', DARK_GREEN)
        color_ten = draw_button(screen, LIGHT_GREEN, 550, 300, 50, 50, '10', DARK_GREEN)
        repeat = draw_button(screen, 'black', 370, 355, 150, 50, 'Herhaling: ', LIGHT_GREEN)
        repeat_yes = draw_button(screen, LIGHT_GREEN, 400, 405, 50, 50, 'Ja', DARK_GREEN)
        repeat_no = draw_button(screen, LIGHT_GREEN, 475, 405, 50, 50, 'Nee', DARK_GREEN)

        # Weergave van de geselecteerde opties mbt moeilijkheidsgraad: geselecteerde optie heeft een rode rand
        # Default instelingen: 6 kleuren en geen herhaling   
        selected_option_color = show_selected_option(screen, select_color_left, select_color_top, select_color_width, select_color_width)
        selected_option_repeat = show_selected_option(screen, select_repeat_left, select_repeat_top, select_repeat_width,select_repeat_height)

        if start_button.collidepoint(pygame.mouse.get_pos()):
            start_button = draw_button(screen, (180, 255, 180), 400, 75, 150, 50, 'Nieuw spel', DARK_GREEN)           
               
        pygame.display.flip()

run_game()

