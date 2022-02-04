/*
 * Copyright (C) 2021 Fabien-B <fabien.bonneval@gmail.com>
 *
 * This file is part of paparazzi
 *
 * paparazzi is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2, or (at your option)
 * any later version.
 *
 * paparazzi is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with paparazzi; see the file COPYING.  If not, see
 * <http://www.gnu.org/licenses/>.
 */

/** @file "modules/conf/conf_storage.h"
 * @author Fabien-B <fabien.bonneval@gmail.com>
 * Store the compressed conf in the flash, and send it to the ground on request.
 */

#ifndef CONF_STORAGE_H
#define CONF_STORAGE_H

#include "stdint.h"

extern void conf_storage_init(void);
extern void conf_storage_datalink(uint8_t* buf);	// SETTING

#endif  // CONF_STORAGE_H
