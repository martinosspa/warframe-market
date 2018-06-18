import riw
import json
from urllib.request import urlopen
def main():
    all_items = riw.request_all_items(isShort=True)
    count = 0
    for item in all_items:
        item_url_name = "mesa%E2%80%99s_waltz" if item["url_name"] == "mesa’s_waltz" else item["url_name"].encode("ascii", "ignore").decode("ascii")
        item_name = item["item_name"].encode("ascii", "ignore").decode("ascii") 
        item_tags = riw.request_tags(item_url_name)
        if not "void relic" in item_tags:
            item_buyer = riw.request_mod(item_url_name, "buy", 0) if "mod" or "arcane enchancements" in items_tags else riw.request_item(item_url_name, "buy")
            item_seller = riw.request_mod(item_url_name, "sell", 0) if "mod" or "arcane enchancements" in items_tags else riw.request_item(item_url_name, "sell")
        if item_buyer and item_seller:
            if item_buyer[0] - item_seller[0] > 10:
                
                difference = item_buyer[0] - item_seller[0]
                
                buyer_name = item_buyer[1]
                buyer_region = item_buyer[2].upper()
                
                seller_name = item_seller[1]
                seller_region = item_seller[2].upper()

                print("Profit: {item} {price}p >> {s}[{s_region}] -> {b}[{b_region}]".format(item=item_name, price=difference, s=seller_name, s_region=seller_region, b=buyer_name, b_region=buyer_region))
        if count % 100 == 0:
            print("{} items scanned".format(count))
        count += 1

if __name__ == "__main__":
    main()
    input("Press any key to exit...")