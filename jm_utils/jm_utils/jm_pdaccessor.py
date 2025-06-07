

import pandas as pd
## qwen

@pd.api.extensions.register_dataframe_accessor("jm")
class CustomAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj


    def infojm(self):
        ''' Get more data similar to self._obj.info() '''
    
        info = {
            'Column': self._obj.columns,
            f'Dtype': self._obj.dtypes.values,
            f'N-Nulls': self._obj.isnull().sum().values,
            f'N-Total': self._obj.count(),
            f'N-Uniques': [
                self._obj[col].nunique() if pd.api.types.is_categorical_dtype(self._obj[col]) or 
                                pd.api.types.is_datetime64_any_dtype(self._obj[col]) or 
                                pd.api.types.is_string_dtype(self._obj[col]) or 
                                pd.api.types.is_numeric_dtype(self._obj[col]) else 0 
                    for col in self._obj.columns
                ],
            }
        self._obj_info = pd.DataFrame(info)
        self._obj_info.index = pd.RangeIndex(start=0, stop=len(self._obj_info), step=1)
        return self._obj_info
    

    def filter_rows(self, **kwargs):
        '''
        Filtra filas según condiciones de igualdad o rango.
        Ejemplos:
            .filter_rows(A=5)
            .filter_rows(B=(2, 8))  # B entre 2 y 8
            .filter_rows(C='texto')
        Args:
            kwargs: Pares clave-valor donde el valor puede ser:
                    - Un valor simple (igualdad)
                    - Una tupla (min, max) (rango)
        Returns:
            pd.DataFrame: DataFrame filtrado.
        '''
        df = self._obj.copy()
        for col, value in kwargs.items():
            if isinstance(value, tuple):
                min_val, max_val = value
                df = df[(df[col] >= min_val) & (df[col] <= max_val)]
            else:
                df = df[df[col] == value]
        return df
    

    def rename_columns(self, mapping=None, prefix="", suffix=""):
        '''
        Renombra columnas con mapeo explícito o añadiendo prefijo/sufijo.
        Args:
            mapping (dict): Mapeo {viejo_nombre: nuevo_nombre}
            prefix (str): Cadena a añadir al inicio de todas las columnas
            suffix (str): Cadena a añadir al final
        Returns:
            pd.DataFrame: DataFrame con columnas renombradas.
        '''
        df = self._obj.copy()
        if mapping:
            df.rename(columns=mapping, inplace=True)
        if prefix or suffix:
            df.columns = [f"{prefix}{col}{suffix}" for col in df.columns]
        return df



    
    if __name__ == "__main__":
        import jm_pdaccessor as jm
        from time import sleep

        # Example usage
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4.0, 5.5, 6.1], 'C': ['x', 'y', 'z']})

        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': ['x', 'y', 'z']})

        df_filtered = df1.jm.filter_rows(A=2, B=(4, 6), C='y')

        # print(df)
        # print()
        # sleep(1)
        # df.jm.multiplicar_numerico(3)
        # print(df)
        # sleep(2)
        # print()
        # print(df.jm.infojm())
        # print()

        input("Press Enter to exit...")
