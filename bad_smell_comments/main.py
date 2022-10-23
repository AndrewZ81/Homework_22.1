class Unit:
    
    def move(self, field, x_axis: int, y_axis: int, direction, is_fly: bool, is_crawl: bool, speed: int = 1):

        if is_fly and is_crawl:
            raise ValueError('Вы ни летите, ни ползёте!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_axis + speed
                new_x = x_axis
            elif direction == 'DOWN':
                new_y = y_axis - speed
                new_x = x_axis
            elif direction == 'LEFT':
                new_y = y_axis
                new_x = x_axis - speed
            elif direction == 'RIGTH':
                new_y = y_axis
                new_x = x_axis + speed
        if is_crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_axis + speed
                new_x = x_axis
            elif direction == 'DOWN':
                new_y = y_axis - speed
                new_x = x_axis
            elif direction == 'LEFT':
                new_y = y_axis
                new_x = x_axis - speed
            elif direction == 'RIGTH':
                new_y = y_axis
                new_x = x_axis + speed

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...