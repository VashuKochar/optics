# Classical treatment of atom field interaction

## Classical field
$$\tag{1} E(\vec r, t) = E_0 e^{i(\omega t - \vec k \cdot \vec r)} $$ 
$$\omega = 2 \pi f$$ 

$E_0$ : Amplitude of electric field (V/m)
$\\ f$: Frequency of electric field (Hz)
$\\ I = \sqrt{\frac{\varepsilon_0}{\mu_0}}|E(\vec r, t)|^2$: Instensity (W/m<sup>2</sup>)


## Electron a spring Model (EOS)
### Equation of motion
$$\tag{2} m \frac{d^2 x}{ dt^2} + b \frac{dx}{dt} + kx = q E(\vec x, t)$$
Note: $E(\vec x,t) \approx E(t) = E_0 e^{i\omega t}$ at electronic scales

$m$: Mass of atom (kg)
$\\ b$: Damping constant (kg/s) 
$\\ k$: Spring constant (kg/s<sup>2</sup>) 
$\\ q$: Charge of electron (V) 

### Comparison with known equation
Same as 
$$\tag{3} \frac{d^2 x}{ dt^2} + \gamma \frac{dx}{dt} + \omega_0^2x = F(t)$$

$\\ \omega_0 = \sqrt \frac{k}{m}$: Oscillator frequency 
$\\ \gamma = \frac{b}{m}$: Damping rate

### Solution
$$\tag{4} x(t) = Ae^{i \omega t}$$
$$A = \frac{q E_0}{m} \frac{1}{(\omega_0^2 - \omega^2 + i \gamma \omega)}$$

### Induced dipole moment
$$\tag{5} p(t) = qx(t)$$

### Macroscopic polarization
$$\tag{6} P(t) = Np(t)$$
$N$: oscillators per unit volume (cm<sup>-3</sup>)

### Maxwell Equation
$$\tag{7} P(t) = \varepsilon_0 \chi E(t)$$
$\chi$: Susceptiblity

Comparing $(6)$ and $(7)$,
$$\tag{8} \chi =\frac{Nq^2}{\varepsilon_0 m} \frac{1}{(\omega_0^2 - \omega^2 + i \gamma \omega)}$$
$$$$

$$\tag{9} \varepsilon = 1+ \chi$$

### Refractive index
$$\tag{10} n=\sqrt {\varepsilon \mu}$$
Since $\mu \approx 1$, 
$$\tag{11} n = \sqrt{\varepsilon}$$

We can also write it as $n = \eta -i \xi$

Real part of complex refractive index ($\eta$) gives dispersion

Imaginary part of complex refractive index ($\xi$) gives absorption

### EM field in the medium
In the medium, $\vec k' = n \vec k$
$$\tag{12} E(\vec r, t) = E_0 e^{i(\omega t - \vec k' \cdot \vec r)} $$ 


### Absorption Coefficient
$$\tag{13} \vec \alpha = 2 Im(\vec k') = -2 \xi \vec k$$

Moreover, 
$$\tag{14} I = I_0 e^{- \vec \alpha \cdot \vec r}$$

### Kramers-Kroning Dispersion relations
After substituting all values and simplifying under the near-resonance assumption ($\omega \approx \omega_0$), 
$$\alpha(\omega) =|\vec \alpha| = \frac{Nq^2}{4 \varepsilon_0 m c} \frac{\gamma}{(\omega_0 - \omega)^2 + (\gamma/2)^2}$$
$$\eta(\omega) =1 + \frac{Nq^2}{4 \varepsilon_0 m \omega_0} \frac{\omega_0 - \omega}{(\omega_0 - \omega)^2 + (\gamma/2)^2}$$

So, we expect a Lorentzian profile for the absorption coefficient ($\alpha$)