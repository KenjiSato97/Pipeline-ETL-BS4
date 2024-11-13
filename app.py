import requests

def fetch_page():
    url = "https://www.mercadolivre.com.br/apple-iphone-16-256-gb-preto-distribuidor-autorizado/p/MLB1040287796?pdp_filters=item_id:MLB3845937933#wid=MLB3845937933&sid=search&is_advertising=true&searchVariation=MLB1040287796&position=1&search_layout=stack&type=pad&tracking_id=48a80342-fe03-45a5-b4e3-331d05c0267e&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=1&ad_click_id=ZDRhMjlmOWEtNmU0Zi00OGM5LTk0NmMtZjUzMmFmOTZlYzgw"
    response = requests.get(url)
    return response.text



if __name__ == "__mani__":
    page_content = fetch_page(url)
    print(page_content)