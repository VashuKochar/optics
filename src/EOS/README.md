# Classical treatment of atom field interaction

## Classical field
$$\tag{1} \vec E(\vec r, t) = \vec E_0 e^{i(\omega t - \vec k \cdot \vec r)} $$ 
$$\omega = 2 \pi f$$ 

$\vec E_0$ : Amplitude vector of electric field (V/m)
$\\ f$: Frequency of electric field (Hz)
$\\ I = \sqrt{\frac{\varepsilon_0}{\mu_0}}| \vec E(\vec r, t)|^2$: Instensity (W/m<sup>2</sup>)


## Electron a spring Model (EOS)
### Equation of motion
$$\tag{2} m \frac{d^2 \vec r}{ dt^2} + b \frac{d \vec r}{dt} + kx = q E(\vec r, t)$$
Note: $E(\vec r,t) \approx E(t) = \vec E_0 e^{i\omega t}$ at electronic scales

$m$: Mass of atom (kg)
$\\ b$: Damping constant (kg/s) 
$\\ k$: Spring constant (kg/s<sup>2</sup>) 
$\\ q$: Charge of electron (V) 

### Comparison with known equation
Same as 
$$\tag{3} \frac{d^2 x}{ dt^2} + \gamma \frac{dx}{dt} + \omega_0^2x = F(t)$$

$\\ \omega_0 = \sqrt \frac{k}{m}$: Oscillator frequency 
$\\ \gamma = \frac{b}{m}$: Damping rate

<!-- ### Boundary condition
EM field switched on at t=0

So, $F(0^-) = 0$ gives
$$x(t) = c_1 e^{-\gamma t/2}(e^{ (\sqrt{\gamma^2 - 4 \omega_0^2} - \gamma) t/2} - c_2 e^{ (\sqrt{\gamma^2 - 4 \omega_0^2} - \gamma) t/2})$$

$$x(0^-) = c_1(1 - c_2)$$ -->

### Solution
$$\tag{4} \vec r(t) = \vec Ae^{i \omega t}$$
$$\vec A = \frac{q \vec E_0}{m} \frac{1}{(\omega_0^2 - \omega^2 + i \gamma \omega)}$$

Similarly,

### Induced dipole moment
$$\tag{5} \vec p(t) = q \vec r(t)$$

### Macroscopic polarization
$$\tag{6} \vec P(t) = N\vec p(t)$$
$N$: oscillators per unit volume (cm<sup>-3</sup>)



We get 
$$\vec P(t) =  \frac{\vec E_0 N q^{2} e^{i t w}}{m \left(i \gamma w - w^{2} + w_{0}^{2}\right)}$$

### Maxwell Equation
$$\tag{7} \vec P(t) = \varepsilon_0 \overline{\overline{\chi}} \vec E(t)$$
$\chi$: Susceptiblity

Comparing $(6)$ and $(7)$,
$$\tag{8} \overline{\overline{\chi}} =\frac{Nq^2}{\varepsilon_0 m} \frac{1}{(\omega_0^2 - \omega^2 + i \gamma \omega)}$$
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
$$\tag{12} \vec E(\vec r, t) = \vec E_0 e^{i(\omega t - \vec k' \cdot \vec r)} $$ 


### Absorption Coefficient
$$\tag{13} \vec \alpha = 2 Im(\vec k') = -2 \xi \vec k$$

Moreover, 
$$\tag{14} I = I_0 e^{- \vec \alpha \cdot \vec r}$$

### Kramers-Kroning Dispersion relations
After substituting all values and simplifying under the near-resonance assumption ($\omega \approx \omega_0$), 
$$\alpha(\omega) =|\vec \alpha| = \frac{Nq^2}{4 \varepsilon_0 m c} \frac{\gamma}{(\omega_0 - \omega)^2 + (\gamma/2)^2}$$

<!-- $$\frac{3.33564095198152 \cdot 10^{-9} N \gamma q^{2} w^{2}}{m \left(\gamma^{2} w^{2} + \left(w^{2} - w_{0}^{2}\right)^{2}\right) \varepsilon_0}$$ -->

$$\eta(\omega) =1 + \frac{Nq^2}{4 \varepsilon_0 m \omega_0} \frac{\omega_0 - \omega}{(\omega_0 - \omega)^2 + (\gamma/2)^2}$$

So, we expect a Lorentzian profile for the absorption coefficient ($\alpha$)