"""
Module Syracuse - Calcul et analyse de la suite de Syracuse.
"""

#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Affiche le graphique de la suite de Syracuse.

    Args:
        lsyr (list): la suite de Syracuse à afficher

    Returns:
        None
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    # votre code ici
    # initialisation des variables
    l = [n]
    while n != 1:
        if n%2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """

    # votre code ici
    k=0
    for i, elt in enumerate(l):
        if elt==1:
            k=i
            break
    return k

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici
    k=0
    for i, elt in enumerate(l):
        if elt<l[0]:
            k=i-1
            break
    return k


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """

    # votre code ici
    return max(l)


#### Fonction principale


def main():
    """
    Fonction principale du module Syracuse.
    
    """

    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

    l = syracuse_l(3)
    print(temps_de_vol(l))
    print(temps_de_vol_en_altitude(l))
    print(altitude_maximale(l))


if __name__ == "__main__":
    main()
