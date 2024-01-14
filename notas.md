#Notas

Para extraer la pagina web y obtener los links hay que hacer tres cosas

1. Obtener la respuesta de la pagina, descargando el html, para esto es necesario llamar a `requests.get()`, que tiene dos parametros, la url, la cual es la direccion del cual queremos el html, y en esete caso, la cabecera, que es un diccionario con las diferentes opciones, que en este caso solo pondremos el agente de chrome para que la peticion sea aceptada. Para obtener el agente solo entra [aqui](https://www.whatismybrowser.com/es/detect/what-is-my-user-agent/)

2. Usar el beautilul soup para que se genere una estructura interesante con la sintaxis `BeautifulSoup(res.text, "html.parser")` donde le pasaremos el texto del html, y le daremos el "html.parser"

3. Para obtener los enlaces de las fotos, en el caso de **[anzmangashd.com](https://www.anzmangashd.com/)** tenemmos este script de ejemplo.


    ```python
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.anzmangashd.com/manga/tales-of-demons-and-gods/461/1"
    recuest_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    res = requests.get(url, headers=recuest_headers)
    soup = BeautifulSoup(res.text, "html.parser")

    tag = soup.find("div", id="all")

    #Uso en lista
    print(tag.contents[1]['data-scr'])

    #Como userlos en un vucle
    for child in tag.children:
        if isinstance(child, bs4.element.Tag):
            print(child['data-src'].strip())

    ```
    Aqui usamos en el soup el metodo `find()` esta funcion, princimalmente, te busca en la etiquetas de html, de forma que si pones `find("div")` te dara el primer div que encuentre. Ademas de esto, se le puede dar un parametro mas para buscar por atributos, de forma que si queremos buscar una etiqueta **div** con el atributo **id = all** el ejmplo seria `find("div, "id="all")`.Que casualemente es justo la estructura que guarda los datos que necesitamos en esta pagina.

    Esta estructura que hemos obtenido es un div con un numeo de imagenes, que son las paginas del capitulo del manga, y tal cual lo extraemos se ve de esta forma.

    ```
    <div id="all" style=" display: none; ">
    <img alt="Tales of Demons and Gods: Chapter 461 - Page 1" class="img-responsive" data-src=" https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBmZUBwQflswY_RYkMMyPgNYL8K_YZK5eFQMHt0aH9TpDEe9LwFXm7l2koCQYe8uYf_fU09ukv6GAzb4xlIYqCx1w6UXnltK2XPGL4Iwgh_kBhEigesqLK0E9MWrE7mL4Y0D43-rE_hmoFqwU-doU3toOH2dJvWxJVwIbrCXVFAwqLMlZDPawBvhEIg7mf/s1600 " src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
    <img alt="Tales of Demons and Gods: Chapter 461 - Page 2" class="img-responsive" data-src=" https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMpCXh_5lx2JAqY5HZj6OqXliOmN472Axq7o1RydJWcGGs-w6n__N6uWz5KJecrCiRPd2RKdPsxSa83-D0Ryvoi2hJOqM8xlb88gnWagiH05_PE_4-H9eSq2qron7wJzLhAHqsgxixRGo8CMpFBQ2AlPMCgdgMDe3HfMf7H4CCRL1CS98eusrjNh835rYo/s1600 " src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
    <img alt="Tales of Demons and Gods: Chapter 461 - Page 3" class="img-responsive" data-src=" https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitUzyfAEzJBy9PAiFi-loaJsBzu9bQO-R8PL1qcXWglRJURCB8TyD0BzuRYNxJTv1qZJkz0auzqxNWorC7IEn83XPbbpljk_fPnAOnUfBdxQ_-wMPIPUMBnooaO1L2N5hZSDFJSlsfpkYFhypqs9sjL_2-iSEWAYV0a_zDyxBg88LwFiytYirikvvp7Z4H/s1600 " src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
    <img alt="Tales of Demons and Gods: Chapter 461 - Page 4" class="img-responsive" data-src=" https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxuruWrxBa3r6v8Bm_KMfgVKjE-18OuRXEp9mosIC0lUT1ehLE3A6LhRMHK0BGM3C4Mj9tUL7QG9eyY9ZR7BGB8wp6vHlgirR0zgqdCk1PRDDPaIP3u9LreiZQbmxHM9CV9C_b4nIHHvA4WMeSPuUS9YykuWrhUDK6FHEl0ADl4OptycFEYgKcPK2cmKPQ/s1600 " src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
    <img alt="Tales of Demons and Gods: Chapter 461 - Page 5" class="img-responsive" data-src=" https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFaE2Cmb8znL-YE8UYet9QhyNXSAih92Q8F2tNQrHE_tzGPaPlzb6b1756zOMjk5S7uctGvgkKvy4IKWXTIag_dPb9Nd0_S-L6baj5hDouTW02zp1Xd1JwsdFfNFVi1PPUkFivIjvVRzSHimimwELyDCPqsz71fUluiXJi1bn8giA_tGOhuzVJq-6oII0B/s1600 " src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
    <img alt="Tales of Demons and Gods: Chapter 461 - Page 6" class="img-responsive" data-src=" https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1frl8S4XtoZZ0SphDD9iJ7X9ecPvsHgb5e2E3ae8XhQ03FTo2yL1ehTU-Aq8zUhVwy5C0e4sjCP3F0DC44EoqlgrkoDBnyrBjAzmJiBJDOmmwSH9CNw2r4NotMQOr06LOgHqb82JW697A1UQs5T3lM9DVkj2ifGf7kq90Be69s_kSS-IfWPLkRVS_ct3A/s1600 " src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
    <img alt="Tales of Demons and Gods: Chapter 461 - Page 7" class="img-responsive" data-src=" https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiqaDJOhwW4oEr4jacEoBLWDT59b8BsyJX1Y6MutfG4BVgt0zyjm9tir92mHERKdI_luYrv03-jb8i8l2qNSYdJe_2dIons3osWo9YQe_pks0FIsKkDVp4as796smv1uwBAaGBXeORhBiH3sEz0CExE9unotQIKKhdmSApt-QJDuSxUbbMSYr4McFc6G3a/s1600 " src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
    <img alt="Tales of Demons and Gods: Chapter 461 - Page 8" class="img-responsive" data-src=" https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtUTIWxWZS5JwaAQ4bUTH1A0kLbvucDYbPd6HeCfkh6b8yCMHPMf2cGbezWsQUYM0_MOvTmhU3TFY_dzNLzQdj88plpOfn0tBmsLuvs9K7FSgkpMrF_PaDGYH3yRRkMNznyV2bXTXZ30NcezSp_B1VFMFizgpwhavZH3YSx3bo676bVbaZWJwROGRGVLzS/s1600 " src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
    <img alt="Tales of Demons and Gods: Chapter 461 - Page 9" class="img-responsive" data-src=" https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRdZayZTPA_5WAYGAcYVHCyZoJg0UB_QHF5ycgVYQ2kNaykKM0zoYbn05ePTXu0PPcXKhf05fcWhiJ9BKvuma-NWfVhK1PkerkN0hRhKvQ1ol7LNwVAN_A2YBefgFB-kDRKhTwLOZsKtuIlXcrb83ImkSCQB3mlmunf9GmufckmXI_tN8N5YRrQBzANukR/s1600 " src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
    <img alt="Tales of Demons and Gods: Chapter 461 - Page 10" class="img-responsive" data-src=" https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDeiZQ42F4dpgpTNADE1viIetOwSJXEGrvId7tZ0Iob8rKxRTlraeFLUnP82tM70l1AGtAZs9cds1E5yo9U9vIWifn312egwyti-tZ-or1syc3WMM52R4GYmnBp7q1vUtGWIw4bPT3OlxpXuM7Y6CbtR2vomAMfSsqhIaSk3vEkSeTtug0AmII3vDun_FP/s1600 " src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
    </div>
    ```
    
    Como podemos observar, los links que necesitamso estan dentro de esa estructura, y la manera mas comoda de estraerla es con el uso del `contents`. Si ponemos este metodo a un objeto soup, este tranforma las etiquetas del mismo nivel como elementos de una lista, por lo que se puede estraer cada etiqueta facilmente. Ademas de este esta el `children`, que es lo mismo pero para recorrer la lista entera.

    Por ultimo, lo que necesitmos es ectraer de la etiqueta imagen el atributo en concreto que es la imagen, y eso lo obtenemos usano unos [] y poniendo denteo el atributo necesario, en este caso, **data-scr**.

    ---

    En este caso, hemos aplicado lo anteriormente mencionado, pero nos encontramos con un probla, aveces, los elementos con el child no son del tipo tag, por que pueden ser solo /n por lo que da erro el codifo anterior, esto se aregla con el sigiente codifo, recordando importar la libreria **bs4**

    ```
    import requests
    import bs4
    from bs4 import BeautifulSoup

    import descargar_imagen
    import PDF_conversor

    url = "https://www.anzmangashd.com/manga/tales-of-demons-and-gods/461/1"
    recuest_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    res = requests.get(url, headers=recuest_headers)
    soup = BeautifulSoup(res.text, "html.parser")

    tag = soup.find("div", id="all")

    #Como userlos en un vucle
    for child in tag.children:
        if isinstance(child, bs4.element.Tag):
            print(child['data-src'].strip())
    ```
    La funcion isinstance comprueba que child sea del tipo bs4.element.Tag