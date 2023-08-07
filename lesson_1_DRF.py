class AssetAPIView (APIView):
    def get(self, request):
        lst = Asset.objects.filter(id__lt=10).values()
        return Response({'assets':list(lst)})

    def post(self, request):
        asset_new = Asset.objects.create(
            ticker =request.data['ticker'],
            isin = request.data['isin'],
            figi = request.data['figi'],
            name_asset = request.data['name_asset'],
            full_name_asset = request.data['full_name_asset'],
            icon = request.data['icon'],
            currency_influence_id = request.data['currency_influence_id'],
            country_asset = request.data['country_asset'],
            type_asset = request.data['type_asset'],
            type_base_asset = request.data['type_base_asset'],
            class_code = request.data['class_code'],
            is_tradable = request.data['is_tradable']
        )
        return Response({'asset': model_to_dict(asset_new)})
