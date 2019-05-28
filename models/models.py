# -*- coding: utf-8 -*-

from odoo import models, fields, api

class WebsiteSocial(models.Model):
	_inherit = 'website'

	social_bitbucket = fields.Char('BitBucket Account')
	social_vimeo = fields.Char('Vimeo Account')
	social_whatsapp = fields.Char('Whatsapp Number')
	social_skype = fields.Char('Skype Account')
	social_twitch = fields.Char('Twitch Account')
	social_reddit = fields.Char('Reddit Account')
	social_tumblr = fields.Char('Tumblr Account')
	social_flickr = fields.Char('Flickr Account')
	social_pinterest = fields.Char('Pinterest Account')
	social_houzz = fields.Char('Houzz Account')

class WebsiteSocialConfig(models.TransientModel):
	_inherit = 'res.config.settings'

	social_bitbucket = fields.Char(related='website_id.social_bitbucket', readonly=False)
	social_vimeo = fields.Char(related='website_id.social_vimeo', readonly=False)
	social_whatsapp = fields.Char(related='website_id.social_whatsapp', readonly=False)
	social_skype = fields.Char(related='website_id.social_skype', readonly=False)
	social_twitch = fields.Char(related='website_id.social_twitch', readonly=False)
	social_reddit = fields.Char(related='website_id.social_reddit', readonly=False)
	social_tumblr = fields.Char(related='website_id.social_tumblr', readonly=False)
	social_flickr = fields.Char(related='website_id.social_flickr', readonly=False)
	social_pinterest = fields.Char(related='website_id.social_pinterest', readonly=False)
	social_houzz = fields.Char(related='website_id.social_houzz', readonly=False)

