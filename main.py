from Dopplershift_analysis import *

'''To do the dopplershifting''' 
##################################################
scan = 4582
manual = False # [21.5,26]
D = Dopplershift_data(mass = 115, scan = scan, voltage_scanning = False, 
	wn_channel = 'wavenumber_1', wn_bounds = [0,99999999999])
data = D.extract_raw_data(devices_to_read = D._devices, path = D._PATH)
data = D.filter_scatter(data = data, filename = 'iscool2', method = 'spline_iscool', ISCOOL_voltage_multiplier =  10000) # apply filter to ISCOOL, for savgol you need to include window_length and polyorder. other options are spline_ISCOOL, avg
data = D.calibrate_CRIS_voltagemeter(data = data, calibration_factor = 1.) 
binned_data = D.bin_data(data = data, freq_multiplier = 1) 
fig,ax = plt.subplots(figsize = (14,9))
fig = D.plot_asymmetric(data = binned_data, fig = fig, ax = ax, save = True, save_format = 'png', fmt = 'r-', label = 'Dopplershifted data') # add save = True if you want to save
plt.show()
D.save_data(binned_data) # saves in D._SAVEPATH, change it in the class variables, defaults to the one in the class

################################################