#module that reads the input and
#constructs the objects that will generate the program's output
import mapquest_in
import mapquest_out

def _input_locations() -> list:
    '''checks how many locations and validates the input'''
    while True:
        location_num = input().strip() #value must be at least 2
        if location_num.isdigit():
            if int(location_num) <= 1:
                print('Please Enter more than One Location')
                continue
            else:
                break
        else:
            print('Please Enter an Integer Value')
            continue
    locations = []
    for n in range(int(location_num)):
        locations.append(input().strip())
    return locations


def _input_outputs() -> list:
    '''checks how many outputs and validates the input'''
    while True:
        output_num = input().strip() #integer must be positive and at least 1
        if output_num.isdigit():
            if int(output_num) <= 0:
                print('Please Enter at least One Output')
                continue
            else:
                break
        else:
            print('Please enter an Integer Value')
            continue
    outputs = []
    for n in range(int(output_num)):
        outputs.append(input().strip().upper())
    return outputs

def run():
    '''asks for input'''
    locations = _input_locations()
    outputs = _input_outputs()
    print()
    try:
        '''checks for error'''
        result = mapquest_in.get_results(mapquest_in.build_search_url(locations))
    except:
        print('\nMAPQUEST ERROR')
    else:
        if result['info']['statuscode'] == 0:
            '''checks if there's a route'''
            for output in outputs:
                '''let x be the CLASS'''
                x = eval('mapquest_out.' + output + '()')
                print(x.get_results(result) + '\n')
        else:
            print('NO ROUTE FOUND\n')
            
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

if __name__ == '__main__':
    run()
