
# One way of speeding this up is to write a method 
# that calls all the default functions itself and
# call that function if True
	
True ==> increment_time()
farm_units == None ==> get_farm_input()
forest_units == None ==> get_forest_input()
True ==> farm_growth()
True ==> forest_growth()
True ==> process_user_input(get_user_input())

