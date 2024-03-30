# view/local_food_map_view.py

from flask import render_template


class LocalFoodMapView:
    @staticmethod
    def render_home_page(farms):
        return render_template('index.html', farms=farms)

    @staticmethod
    def render_farm_page(farm):
        return render_template('show_farm.html', farm=farm)

    @staticmethod
    def render_not_found(error_message):
        # Render a 404 error page with the given error message
        return render_template('404.html', error_message=error_message), 404

    @staticmethod
    def render_farms_sorted_page(farms):
        # This will render a template that lists farms in order, including showing distances
        return render_template('sorted_farms.html', farms=farms)
