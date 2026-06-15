# 🏆 Predicción completa del Mundial 2026 — los 104 partidos

Generado con el modelo de este repositorio: regresores XGBoost (Tweedie) de goles + clasificador 1X2 XGBoost calibrado (isotónico), predicción a sede neutral con "efecto espejo", temperatura `T=0.27` en grupos y `T=0.5` en eliminatorias, y simulación de **Monte Carlo de 10.000 mundiales** para las probabilidades por selección.

> ⚠️ Predicción generada el 12-jun-2026, con los datos del repo (anteriores al torneo). La asignación de mejores terceros al cuadro usa la simplificación del notebook (ranking 1º-8º a huecos fijos), no la tabla oficial de la FIFA.

## Resumen

| | |
|---|---|
| 🥇 **Campeón predicho** | **🇪🇸 España** |
| 🥈 Subcampeón | 🇦🇷 Argentina |
| 🥉 Tercer puesto | 🇫🇷 Francia |

### Probabilidades de ser campeón (Top 10, Monte Carlo)

| # | Selección | Campeón | Final | Semis | Cuartos |
|---|---|---|---|---|---|
| 1 | 🇫🇷 Francia | **26.5%** | 38.6% | 60.2% | 70.9% |
| 2 | 🇪🇸 España | **21.5%** | 33.8% | 54.8% | 63.7% |
| 3 | 🇦🇷 Argentina | **17.7%** | 34.2% | 50.8% | 69.9% |
| 4 | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | **16.2%** | 34.8% | 62.8% | 80.4% |
| 5 | 🇵🇹 Portugal | **4.6%** | 13.8% | 31.9% | 69.7% |
| 6 | 🇩🇪 Alemania | **4.1%** | 8.8% | 17.8% | 29.6% |
| 7 | 🇧🇪 Bélgica | **3.3%** | 8.9% | 27.0% | 77.5% |
| 8 | 🇳🇱 Países Bajos | **2.2%** | 6.8% | 16.1% | 46.5% |
| 9 | 🇭🇷 Croacia | **1.0%** | 4.0% | 13.8% | 28.0% |
| 10 | 🇧🇷 Brasil | **0.7%** | 3.9% | 11.9% | 39.4% |

## Fase de grupos — 72 partidos

Marcador = marcador exacto más probable según los goles esperados del modelo, condicionado al resultado 1X2 más probable.

### Grupo A

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-11 | 🇲🇽 México – 🇿🇦 Sudáfrica | **1-0** | 85% | 13% | 2% |
| 06-11 | 🇰🇷 Corea del Sur – 🇨🇿 República Checa | **1-0** | 69% | 22% | 8% |
| 06-18 | 🇨🇿 República Checa – 🇿🇦 Sudáfrica | **0-1** | 39% | 18% | 43% |
| 06-18 | 🇲🇽 México – 🇰🇷 Corea del Sur | **1-0** | 64% | 28% | 8% |
| 06-24 | 🇿🇦 Sudáfrica – 🇰🇷 Corea del Sur | **0-1** | 4% | 27% | 69% |
| 06-24 | 🇨🇿 República Checa – 🇲🇽 México | **0-1** | 3% | 12% | 86% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇲🇽 México ✅ | 9 | +2.84 |
| 2 | 🇰🇷 Corea del Sur ✅ | 6 | +1.19 |
| 3 | 🇿🇦 Sudáfrica 🟡 | 3 | -2.43 |
| 4 | 🇨🇿 República Checa | 0 | -1.60 |

### Grupo B

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-12 | 🇨🇦 Canadá – 🇧🇦 Bosnia-Herzegovina | **1-0** | 77% | 21% | 2% |
| 06-13 | 🇶🇦 Catar – 🇨🇭 Suiza | **0-1** | 1% | 10% | 89% |
| 06-18 | 🇨🇭 Suiza – 🇧🇦 Bosnia-Herzegovina | **2-1** | 72% | 20% | 8% |
| 06-18 | 🇨🇦 Canadá – 🇶🇦 Catar | **1-0** | 72% | 25% | 3% |
| 06-24 | 🇧🇦 Bosnia-Herzegovina – 🇶🇦 Catar | **1-0** | 43% | 24% | 34% |
| 06-24 | 🇨🇭 Suiza – 🇨🇦 Canadá | **1-1** | 35% | 36% | 29% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇨🇭 Suiza ✅ | 5 | +0.90 |
| 2 | 🇨🇦 Canadá ✅ | 5 | +0.40 |
| 3 | 🇧🇦 Bosnia-Herzegovina 🟡 | 4 | -0.48 |
| 4 | 🇶🇦 Catar | 1 | -0.82 |

### Grupo C

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-13 | 🇧🇷 Brasil – 🇲🇦 Marruecos | **0-1** | 30% | 21% | 49% |
| 06-13 | 🇭🇹 Haití – 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia | **0-1** | 4% | 11% | 84% |
| 06-19 | 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia – 🇲🇦 Marruecos | **0-1** | 3% | 14% | 83% |
| 06-19 | 🇧🇷 Brasil – 🇭🇹 Haití | **2-0** | 98% | 1% | 0% |
| 06-24 | 🇲🇦 Marruecos – 🇭🇹 Haití | **2-0** | 97% | 2% | 1% |
| 06-24 | 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia – 🇧🇷 Brasil | **1-2** | 1% | 11% | 88% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇧🇷 Brasil ✅ | 7 | +2.85 |
| 2 | 🇲🇦 Marruecos ✅ | 7 | +2.59 |
| 3 | 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia 🟡 | 3 | -0.73 |
| 4 | 🇭🇹 Haití | 0 | -4.71 |

### Grupo D

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-12 | 🇺🇸 EE. UU. – 🇵🇾 Paraguay | **1-0** | 59% | 32% | 9% |
| 06-13 | 🇦🇺 Australia – 🇹🇷 Turquía | **0-1** | 31% | 21% | 48% |
| 06-19 | 🇺🇸 EE. UU. – 🇦🇺 Australia | **1-0** | 58% | 24% | 18% |
| 06-19 | 🇹🇷 Turquía – 🇵🇾 Paraguay | **1-0** | 89% | 9% | 2% |
| 06-25 | 🇵🇾 Paraguay – 🇦🇺 Australia | **0-1** | 7% | 13% | 80% |
| 06-25 | 🇹🇷 Turquía – 🇺🇸 EE. UU. | **1-0** | 48% | 24% | 28% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇺🇸 EE. UU. ✅ | 6 | +3.14 |
| 2 | 🇦🇺 Australia ✅ | 6 | +2.01 |
| 3 | 🇹🇷 Turquía 🟡 | 6 | -1.08 |
| 4 | 🇵🇾 Paraguay | 0 | -4.07 |

### Grupo E

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-14 | 🇩🇪 Alemania – 🇨🇼 Curazao | **2-0** | 98% | 1% | 0% |
| 06-14 | 🇨🇮 Costa de Marfil – 🇪🇨 Ecuador | **1-0** | 61% | 22% | 18% |
| 06-20 | 🇩🇪 Alemania – 🇨🇮 Costa de Marfil | **1-0** | 85% | 13% | 2% |
| 06-20 | 🇪🇨 Ecuador – 🇨🇼 Curazao | **1-0** | 92% | 7% | 1% |
| 06-25 | 🇨🇼 Curazao – 🇨🇮 Costa de Marfil | **0-1** | 0% | 4% | 96% |
| 06-25 | 🇪🇨 Ecuador – 🇩🇪 Alemania | **0-1** | 1% | 11% | 88% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇩🇪 Alemania ✅ | 9 | +7.57 |
| 2 | 🇨🇮 Costa de Marfil ✅ | 6 | +1.64 |
| 3 | 🇪🇨 Ecuador 🟡 | 3 | -0.89 |
| 4 | 🇨🇼 Curazao | 0 | -8.32 |

### Grupo F

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-14 | 🇳🇱 Países Bajos – 🇯🇵 Japón | **1-0** | 68% | 24% | 9% |
| 06-14 | 🇸🇪 Suecia – 🇹🇳 Túnez | **1-0** | 47% | 30% | 22% |
| 06-20 | 🇳🇱 Países Bajos – 🇸🇪 Suecia | **2-1** | 87% | 12% | 1% |
| 06-20 | 🇹🇳 Túnez – 🇯🇵 Japón | **0-1** | 1% | 4% | 94% |
| 06-25 | 🇯🇵 Japón – 🇸🇪 Suecia | **1-0** | 90% | 9% | 1% |
| 06-25 | 🇹🇳 Túnez – 🇳🇱 Países Bajos | **0-1** | 0% | 8% | 91% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇳🇱 Países Bajos ✅ | 7 | +1.77 |
| 2 | 🇯🇵 Japón ✅ | 7 | +1.25 |
| 3 | 🇸🇪 Suecia 🟡 | 3 | +2.48 |
| 4 | 🇹🇳 Túnez | 0 | -5.50 |

### Grupo G

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-15 | 🇧🇪 Bélgica – 🇪🇬 Egipto | **1-0** | 89% | 10% | 1% |
| 06-15 | 🇮🇷 Irán – 🇳🇿 Nueva Zelanda | **1-0** | 91% | 8% | 1% |
| 06-21 | 🇧🇪 Bélgica – 🇮🇷 Irán | **1-0** | 74% | 24% | 3% |
| 06-21 | 🇳🇿 Nueva Zelanda – 🇪🇬 Egipto | **0-1** | 2% | 9% | 89% |
| 06-26 | 🇳🇿 Nueva Zelanda – 🇧🇪 Bélgica | **0-2** | 0% | 2% | 98% |
| 06-26 | 🇪🇬 Egipto – 🇮🇷 Irán | **0-1** | 6% | 16% | 79% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇧🇪 Bélgica ✅ | 9 | +3.13 |
| 2 | 🇮🇷 Irán ✅ | 6 | +0.83 |
| 3 | 🇪🇬 Egipto 🟡 | 3 | -0.64 |
| 4 | 🇳🇿 Nueva Zelanda | 0 | -3.32 |

### Grupo H

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-15 | 🇪🇸 España – 🇨🇻 Cabo Verde | **2-0** | 91% | 8% | 0% |
| 06-15 | 🇸🇦 Arabia Saudí – 🇺🇾 Uruguay | **0-2** | 0% | 3% | 97% |
| 06-21 | 🇪🇸 España – 🇸🇦 Arabia Saudí | **2-0** | 98% | 2% | 0% |
| 06-21 | 🇺🇾 Uruguay – 🇨🇻 Cabo Verde | **1-0** | 85% | 12% | 3% |
| 06-26 | 🇺🇾 Uruguay – 🇪🇸 España | **0-1** | 1% | 17% | 82% |
| 06-26 | 🇨🇻 Cabo Verde – 🇸🇦 Arabia Saudí | **1-0** | 71% | 16% | 13% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇪🇸 España ✅ | 7 | +3.13 |
| 2 | 🇺🇾 Uruguay ✅ | 6 | +1.22 |
| 3 | 🇨🇻 Cabo Verde 🟡 | 4 | -0.52 |
| 4 | 🇸🇦 Arabia Saudí | 0 | -3.83 |

### Grupo I

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-16 | 🇫🇷 Francia – 🇸🇳 Senegal | **1-0** | 86% | 12% | 2% |
| 06-16 | 🇮🇶 Irak – 🇳🇴 Noruega | **0-1** | 1% | 4% | 96% |
| 06-22 | 🇫🇷 Francia – 🇮🇶 Irak | **2-0** | 99% | 1% | 0% |
| 06-22 | 🇳🇴 Noruega – 🇸🇳 Senegal | **0-1** | 13% | 27% | 61% |
| 06-26 | 🇳🇴 Noruega – 🇫🇷 Francia | **0-2** | 1% | 6% | 93% |
| 06-26 | 🇸🇳 Senegal – 🇮🇶 Irak | **1-0** | 96% | 3% | 1% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇫🇷 Francia ✅ | 9 | +3.92 |
| 2 | 🇸🇳 Senegal ✅ | 6 | +1.09 |
| 3 | 🇳🇴 Noruega 🟡 | 3 | -0.93 |
| 4 | 🇮🇶 Irak | 0 | -4.08 |

### Grupo J

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-16 | 🇦🇷 Argentina – 🇩🇿 Argelia | **1-0** | 87% | 12% | 1% |
| 06-16 | 🇦🇹 Austria – 🇯🇴 Jordania | **2-0** | 99% | 1% | 0% |
| 06-22 | 🇦🇷 Argentina – 🇦🇹 Austria | **1-0** | 73% | 21% | 6% |
| 06-22 | 🇯🇴 Jordania – 🇩🇿 Argelia | **0-1** | 2% | 4% | 95% |
| 06-27 | 🇩🇿 Argelia – 🇦🇹 Austria | **0-1** | 17% | 25% | 58% |
| 06-27 | 🇯🇴 Jordania – 🇦🇷 Argentina | **0-2** | 0% | 1% | 99% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇦🇷 Argentina ✅ | 9 | +3.65 |
| 2 | 🇦🇹 Austria ✅ | 6 | +0.88 |
| 3 | 🇩🇿 Argelia 🟡 | 3 | +0.01 |
| 4 | 🇯🇴 Jordania | 0 | -4.54 |

### Grupo K

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-17 | 🇵🇹 Portugal – 🇨🇩 RD Congo | **1-0** | 94% | 4% | 1% |
| 06-17 | 🇺🇿 Uzbekistán – 🇨🇴 Colombia | **0-1** | 2% | 9% | 90% |
| 06-23 | 🇵🇹 Portugal – 🇺🇿 Uzbekistán | **2-0** | 94% | 6% | 1% |
| 06-23 | 🇨🇴 Colombia – 🇨🇩 RD Congo | **1-0** | 88% | 9% | 4% |
| 06-27 | 🇨🇩 RD Congo – 🇺🇿 Uzbekistán | **1-0** | 62% | 13% | 25% |
| 06-27 | 🇨🇴 Colombia – 🇵🇹 Portugal | **0-1** | 4% | 14% | 81% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🇵🇹 Portugal ✅ | 9 | +2.92 |
| 2 | 🇨🇴 Colombia ✅ | 6 | +1.11 |
| 3 | 🇨🇩 RD Congo 🟡 | 3 | -1.46 |
| 4 | 🇺🇿 Uzbekistán | 0 | -2.57 |

### Grupo L

| Fecha | Partido | Pred. | P(1) | P(X) | P(2) |
|---|---|:-:|--:|--:|--:|
| 06-17 | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra – 🇭🇷 Croacia | **2-1** | 67% | 26% | 6% |
| 06-17 | 🇬🇭 Ghana – 🇵🇦 Panamá | **0-1** | 4% | 18% | 78% |
| 06-23 | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra – 🇬🇭 Ghana | **2-0** | 98% | 2% | 0% |
| 06-23 | 🇵🇦 Panamá – 🇭🇷 Croacia | **0-1** | 1% | 7% | 91% |
| 06-27 | 🇭🇷 Croacia – 🇬🇭 Ghana | **2-0** | 97% | 3% | 0% |
| 06-27 | 🇵🇦 Panamá – 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | **0-2** | 0% | 3% | 97% |

| Pos | Equipo | Pts | DG (xG) |
|---|---|--:|--:|
| 1 | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra ✅ | 9 | +3.58 |
| 2 | 🇭🇷 Croacia ✅ | 6 | +2.22 |
| 3 | 🇵🇦 Panamá 🟡 | 3 | -2.15 |
| 4 | 🇬🇭 Ghana | 0 | -3.65 |

✅ clasificado directo · 🟡 tercero (pasan los 8 mejores)

## Eliminatorias — 32 partidos

Si el empate es el resultado más probable, el cruce se decide por penaltis a favor del equipo con mayor probabilidad de victoria.

### Dieciseisavos de final (16 cruces) · *28 jun - 3 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇩🇪 Alemania – 🇹🇷 Turquía | **2-1** | **🇩🇪 Alemania** | 63% | 26% | 12% |
| 🇫🇷 Francia – 🇧🇦 Bosnia-Herzegovina | **2-0** | **🇫🇷 Francia** | 88% | 9% | 2% |
| 🇰🇷 Corea del Sur – 🇨🇦 Canadá | **1-1 (pen)** | **🇰🇷 Corea del Sur** | 39% | 40% | 21% |
| 🇳🇱 Países Bajos – 🇲🇦 Marruecos | **1-0** | **🇳🇱 Países Bajos** | 42% | 28% | 29% |
| 🇨🇴 Colombia – 🇭🇷 Croacia | **0-1** | **🇭🇷 Croacia** | 12% | 25% | 63% |
| 🇪🇸 España – 🇦🇹 Austria | **2-1** | **🇪🇸 España** | 53% | 35% | 11% |
| 🇺🇸 EE. UU. – 🇨🇻 Cabo Verde | **1-0** | **🇺🇸 EE. UU.** | 59% | 24% | 17% |
| 🇧🇪 Bélgica – 🇸🇪 Suecia | **2-1** | **🇧🇪 Bélgica** | 72% | 24% | 4% |
| 🇧🇷 Brasil – 🇯🇵 Japón | **1-0** | **🇧🇷 Brasil** | 52% | 29% | 19% |
| 🇨🇮 Costa de Marfil – 🇸🇳 Senegal | **0-1** | **🇸🇳 Senegal** | 17% | 28% | 54% |
| 🇲🇽 México – 🇩🇿 Argelia | **1-0** | **🇲🇽 México** | 51% | 30% | 20% |
| 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra – 🇪🇬 Egipto | **1-0** | **🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra** | 80% | 17% | 3% |
| 🇦🇷 Argentina – 🇺🇾 Uruguay | **1-0** | **🇦🇷 Argentina** | 66% | 23% | 10% |
| 🇦🇺 Australia – 🇮🇷 Irán | **0-1** | **🇮🇷 Irán** | 15% | 24% | 61% |
| 🇨🇭 Suiza – 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia | **2-1** | **🇨🇭 Suiza** | 60% | 26% | 15% |
| 🇵🇹 Portugal – 🇪🇨 Ecuador | **1-0** | **🇵🇹 Portugal** | 66% | 23% | 10% |

### Octavos de final · *4 - 7 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇩🇪 Alemania – 🇫🇷 Francia | **1-2** | **🇫🇷 Francia** | 19% | 34% | 47% |
| 🇰🇷 Corea del Sur – 🇳🇱 Países Bajos | **0-1** | **🇳🇱 Países Bajos** | 10% | 28% | 63% |
| 🇭🇷 Croacia – 🇪🇸 España | **1-2** | **🇪🇸 España** | 12% | 41% | 47% |
| 🇺🇸 EE. UU. – 🇧🇪 Bélgica | **0-1** | **🇧🇪 Bélgica** | 6% | 25% | 69% |
| 🇧🇷 Brasil – 🇸🇳 Senegal | **0-1** | **🇸🇳 Senegal** | 34% | 29% | 36% |
| 🇲🇽 México – 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | **0-1** | **🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra** | 10% | 21% | 69% |
| 🇦🇷 Argentina – 🇮🇷 Irán | **1-0** | **🇦🇷 Argentina** | 68% | 24% | 8% |
| 🇨🇭 Suiza – 🇵🇹 Portugal | **1-2** | **🇵🇹 Portugal** | 14% | 27% | 58% |

### Cuartos de final · *9 - 11 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇫🇷 Francia – 🇳🇱 Países Bajos | **2-1** | **🇫🇷 Francia** | 50% | 33% | 17% |
| 🇪🇸 España – 🇧🇪 Bélgica | **2-1** | **🇪🇸 España** | 47% | 44% | 10% |
| 🇸🇳 Senegal – 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | **0-1** | **🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra** | 16% | 28% | 57% |
| 🇦🇷 Argentina – 🇵🇹 Portugal | **1-1 (pen)** | **🇦🇷 Argentina** | 39% | 40% | 21% |

### Semifinales · *14 - 15 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇫🇷 Francia – 🇪🇸 España | **1-1 (pen)** | **🇪🇸 España** | 31% | 36% | 33% |
| 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra – 🇦🇷 Argentina | **1-1 (pen)** | **🇦🇷 Argentina** | 26% | 38% | 36% |

### Partido por el 3er puesto · *18 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇫🇷 Francia – 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | **2-1** | **🇫🇷 Francia** | 46% | 34% | 20% |

### 🏆 Gran Final — MetLife Stadium, Nueva York/Nueva Jersey · *19 jul*

| Cruce | Pred. | Avanza | P(1) | P(X) | P(2) |
|---|:-:|---|--:|--:|--:|
| 🇪🇸 España – 🇦🇷 Argentina | **1-1 (pen)** | **🇪🇸 España** | 31% | 41% | 28% |

## Probabilidades por selección — 10.000 mundiales simulados

| Selección | Pasa grupos | Octavos | Cuartos | Semis | Final | 🏆 Campeón |
|---|--:|--:|--:|--:|--:|--:|
| 🇫🇷 Francia | 100.0% | 94.6% | 70.9% | 60.2% | 38.6% | **26.5%** |
| 🇪🇸 España | 100.0% | 77.7% | 63.7% | 54.8% | 33.8% | **21.5%** |
| 🇦🇷 Argentina | 100.0% | 78.6% | 69.9% | 50.8% | 34.2% | **17.7%** |
| 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | 100.0% | 93.0% | 80.4% | 62.8% | 34.8% | **16.2%** |
| 🇵🇹 Portugal | 100.0% | 85.7% | 69.7% | 31.9% | 13.8% | **4.6%** |
| 🇩🇪 Alemania | 100.0% | 88.5% | 29.6% | 17.8% | 8.8% | **4.1%** |
| 🇧🇪 Bélgica | 100.0% | 89.1% | 77.5% | 27.0% | 8.9% | **3.3%** |
| 🇳🇱 Países Bajos | 99.8% | 57.3% | 46.5% | 16.1% | 6.8% | **2.2%** |
| 🇭🇷 Croacia | 99.8% | 81.3% | 28.0% | 13.8% | 4.0% | **1.0%** |
| 🇧🇷 Brasil | 99.9% | 68.4% | 39.4% | 11.9% | 3.9% | **0.7%** |
| 🇸🇳 Senegal | 98.5% | 69.4% | 36.6% | 11.7% | 3.6% | **0.7%** |
| 🇲🇦 Marruecos | 99.9% | 48.8% | 35.0% | 8.1% | 2.4% | **0.4%** |
| 🇦🇹 Austria | 99.5% | 29.2% | 12.4% | 5.0% | 1.4% | **0.4%** |
| 🇲🇽 México | 100.0% | 77.9% | 15.4% | 5.3% | 1.2% | **0.2%** |
| 🇺🇾 Uruguay | 99.6% | 20.4% | 8.3% | 2.6% | 0.5% | **0.1%** |
| 🇯🇵 Japón | 99.9% | 27.7% | 12.3% | 2.1% | 0.4% | **0.1%** |
| 🇮🇷 Irán | 98.6% | 67.8% | 14.2% | 4.2% | 0.7% | **0.1%** |
| 🇨🇭 Suiza | 88.9% | 56.3% | 15.1% | 2.6% | 0.4% | **0.1%** |
| 🇨🇮 Costa de Marfil | 100.0% | 31.2% | 9.0% | 1.8% | 0.4% | **0.0%** |
| 🇨🇴 Colombia | 99.0% | 20.3% | 6.1% | 1.7% | 0.3% | **0.0%** |
| 🇳🇴 Noruega | 71.0% | 20.8% | 6.6% | 1.4% | 0.2% | **0.0%** |
| 🇺🇸 EE. UU. | 99.9% | 50.4% | 6.6% | 0.8% | 0.1% | **0.0%** |
| 🇹🇷 Turquía | 79.1% | 27.1% | 6.6% | 1.7% | 0.4% | **0.0%** |
| 🇰🇷 Corea del Sur | 100.0% | 66.0% | 11.4% | 0.7% | 0.1% | **0.0%** |
| 🇩🇿 Argelia | 94.9% | 18.4% | 3.5% | 0.6% | 0.0% | **0.0%** |
| 🇨🇦 Canadá | 89.0% | 38.9% | 7.8% | 0.8% | 0.1% | **0.0%** |
| 🇦🇺 Australia | 99.8% | 34.0% | 5.0% | 0.6% | 0.1% | **0.0%** |
| 🇪🇨 Ecuador | 70.4% | 14.5% | 4.0% | 0.6% | 0.0% | **0.0%** |
| 🇪🇬 Egipto | 87.8% | 15.2% | 2.4% | 0.2% | 0.0% | **0.0%** |
| 🇸🇪 Suecia | 99.7% | 13.1% | 1.5% | 0.1% | 0.0% | **0.0%** |
| 🇨🇻 Cabo Verde | 74.4% | 8.1% | 0.9% | 0.1% | 0.0% | **0.0%** |
| 🇨🇿 República Checa | 9.4% | 1.6% | 0.2% | 0.0% | 0.0% | **0.0%** |
| 🇿🇦 Sudáfrica | 15.2% | 2.6% | 0.4% | 0.0% | 0.0% | **0.0%** |
| 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia | 93.5% | 11.8% | 1.5% | 0.1% | 0.0% | **0.0%** |
| 🇧🇦 Bosnia-Herzegovina | 51.5% | 6.2% | 0.6% | 0.0% | 0.0% | **0.0%** |
| 🇨🇩 RD Congo | 20.4% | 2.4% | 0.4% | 0.0% | 0.0% | **0.0%** |
| 🇵🇦 Panamá | 12.5% | 1.5% | 0.2% | 0.0% | 0.0% | **0.0%** |
| 🇸🇦 Arabia Saudí | 0.7% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇶🇦 Catar | 40.2% | 3.7% | 0.2% | 0.0% | 0.0% | **0.0%** |
| 🇨🇼 Curazao | 0.1% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇬🇭 Ghana | 0.5% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇭🇹 Haití | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇮🇶 Irak | 0.1% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇯🇴 Jordania | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇳🇿 Nueva Zelanda | 0.3% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇵🇾 Paraguay | 1.0% | 0.1% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇹🇳 Túnez | 0.1% | 0.0% | 0.0% | 0.0% | 0.0% | **0.0%** |
| 🇺🇿 Uzbekistán | 5.0% | 0.4% | 0.0% | 0.0% | 0.0% | **0.0%** |

## Validación con los partidos ya jugados

| Partido | Predicción (1X2 máx) | Resultado real | ¿Acierto? |
|---|:-:|:-:|:-:|
| 🇲🇽 México – 🇿🇦 Sudáfrica | México (85%) | 2-0 | ✅ |
| 🇰🇷 Corea del Sur – 🇨🇿 República Checa | Corea del Sur (69%) | 2-1 | ✅ |
| 🇨🇦 Canadá – 🇧🇦 Bosnia-Herzegovina | Canadá (77%) | 1-1 | ❌ |
| 🇶🇦 Catar – 🇨🇭 Suiza | Suiza (89%) | 1-1 | ❌ |
| 🇧🇷 Brasil – 🇲🇦 Marruecos | Marruecos (49%) | 1-1 | ❌ |
| 🇭🇹 Haití – 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Escocia | Escocia (84%) | 0-1 | ✅ |
| 🇺🇸 EE. UU. – 🇵🇾 Paraguay | EE. UU. (59%) | 4-1 | ✅ |
| 🇦🇺 Australia – 🇹🇷 Turquía | Turquía (48%) | 2-0 | ❌ |
| 🇩🇪 Alemania – 🇨🇼 Curazao | Alemania (98%) | 7-1 | ✅ |
| 🇨🇮 Costa de Marfil – 🇪🇨 Ecuador | Costa de Marfil (61%) | 1-0 | ✅ |
| 🇳🇱 Países Bajos – 🇯🇵 Japón | Países Bajos (68%) | 2-2 | ❌ |
| 🇸🇪 Suecia – 🇹🇳 Túnez | Suecia (47%) | 5-1 | ✅ |
| 🇪🇸 España – 🇨🇻 Cabo Verde | España (91%) | 0-0 | ❌ |

**Aciertos de ganador: 7/13 (54%).** Las probabilidades de campeón y de clasificación de arriba ya están *condicionadas* a estos resultados: los partidos jugados se fijan y solo se simulan los que faltan.

---
*Predicciones generadas automáticamente con `prediccion_mundial.py`. El fútbol, por suerte, no entiende de modelos.* ⚽