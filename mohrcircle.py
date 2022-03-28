import numpy as np
import matplotlib.pyplot as plt

sigma_x = -0.08
sigma_y = 0.04
tau_xy = 0.062
r = np.sqrt((0.5 * (sigma_x - sigma_y))**2 + (tau_xy)**2)
sigma_avg = (sigma_x + sigma_y)/2
angle = np.linspace(0, 2* np.pi, 360)
x = sigma_avg + r * np.cos(angle)
y = r * np.sin(angle)
cal_angle = np.pi/3

theta_p = (np.arctan((tau_xy)/(sigma_x-sigma_avg)))
theta_p_rad = (np.arctan((tau_xy)/(sigma_x-sigma_avg))) * -57.2958/2

theta_x = sigma_avg + r * np.cos(theta_p)
theta_xy = r * np.sin(theta_p)

sigma_angle = (sigma_avg + r * np.cos(theta_p + cal_angle))
tau_angle = (r * np.sin(theta_p + cal_angle))

max_principal_stress = sigma_avg + r
min_principal_stress = sigma_avg - r
max_shear_stress = r
min_shear_stress = -r
plt.axvline(color = 'k')
plt.axhline(color = 'k')

plt.plot(x,y)

plt.title('Mohrs Circle ', fontsize = 25)
plt.ylabel(r'$\tau$', fontsize = 20)
plt.xlabel(r'$\sigma$', fontsize = 20)
plt.fill_between(x, y, color = 'k', alpha = 0.1)

plt.plot(sigma_avg,[0], marker = 'o', color = 'g')
plt.plot([sigma_x, sigma_y], [tau_xy, -tau_xy], color = 'r')
plt.plot([sigma_avg, 2*sigma_avg - sigma_angle], [0, -tau_angle], color = 'b')
plt.plot(2*sigma_avg - sigma_angle, -tau_angle, marker = 'o', color = 'r')

plt.plot(sigma_x,tau_xy, marker = 'o', color = 'g')

plt.text(max_principal_stress, 0, r'$\sigma_{max}$', va = 'bottom', ha = 'right', fontsize = 11)
plt.text(min_principal_stress, 0, r'$\sigma_{min}$', ha = 'left', va = 'bottom', fontsize = 11)
plt.text(sigma_avg, max_shear_stress, r'$\tau_{max}$', va='top', ha = 'center', fontsize = 11) 
plt.text(sigma_avg, min_shear_stress, r'$\tau_{min}$', va='bottom', ha = 'center', fontsize = 11)
plt.text(2*sigma_avg - sigma_angle, -tau_angle, r'($\sigma_{30}$, $\tau_{30}$)', va='top', ha = 'left', fontsize = 13)  
plt.tight_layout()
plt.grid()
plt.show()