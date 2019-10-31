"""BouncyNumber
En este modulo se trata de encontrar el número mínimo para la proporción de bouncy number cuando sea
exactamente 99%.

Example
-------
A continuacion demuestro como se debe ejecutar el archivo::

    $ python bouncy_number.py
"""


class BouncyNumber:

    @staticmethod
    def is_bouncy(number: int)->bool:
        """La funcion is_bouncy se encarga de verificar si es un bouncy number.

        Parameters
        ----------
        number : int
            Numero que varia y el cual sera verificado.

        Returns
        -------
        bool
            True si es un bouncy number, False si no es un bouncy number.
        """
        validate_increment = False
        validate_decrement = False
        last_number = int(number % 10)
        number = int(number / 10)
        while number > 0:
            next_number = int(number % 10)
            number = int(number / 10)
            if next_number > last_number:
                validate_decrement = True
            elif next_number < last_number:
                validate_increment = True
            if validate_decrement and validate_increment:
                break
            last_number = next_number
        return validate_increment and validate_decrement

    def search_number(self)->int:
        """La funcion search_number se encarga de buscar cual es el bouncy number cuando sea exactamente 99%.

        Teniendo claro que el 21780 es el bouncy number al 90% tomo eso como partida y la proporcion seria 19602 ya que
        este seria el 90% de 21780.

        Returns
        -------
        int
            El bouncy number que considero que tiene la proporcion de 99%.
        """
        bouncy_number = 19602
        pointer_number = 21780
        while (99*pointer_number) > (bouncy_number*100):
            pointer_number += 1
            if self.is_bouncy(pointer_number):
                bouncy_number += 1
        return pointer_number


number_result = BouncyNumber().search_number()
print(f"Solucion --> [{number_result}]", flush=True)
