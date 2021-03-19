from flask import (
  Blueprint, render_template
  )

bp = Blueprint('projects', __name__, url_prefix='/projects')


@bp.route('/stock-query')
def stocks():
  return render_template('projects/stocks.html')

@bp.route('/pathtracer')
def pathtracer():
  return render_template('projects/pathtracer.html')

@bp.route('/clothsim')
def clothsim():
  return render_template('projects/clothsim.html')

@bp.route('/volumetric-scattering')
def volumetric_scattering():
  return render_template('projects/volumetric_scattering.html')