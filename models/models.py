# -*- coding: utf-8 -*-

from odoo import models, fields, api

class WebsiteSocial(models.Model):
	_inherit = 'website'

	social_instagram = fields.Char('Instagram Account')
	social_bitbucket = fields.Char('BitBucket Account')
	social_vimeo = fields.Char('Vimeo Account')
	social_whatsapp = fields.Char('Whatsapp Number')
	social_skype = fields.Char('Skype Account')
	social_twitch = fields.Char('Twitch Account')
	social_reddit = fields.Char('Reddit Account')
	social_tumblr = fields.Char('Tumblr Account')
	social_flickr = fields.Char('Flickr Account')

class WebsiteSocialConfig(models.TransientModel):
        _inherit = 'website.config.settings'

        social_instagram = fields.Char(related='website_id.social_instagram')
        social_bitbucket = fields.Char(related='website_id.social_bitbucket')
        social_vimeo = fields.Char(related='website_id.social_vimeo')
        social_whatsapp = fields.Char(related='website_id.social_whatsapp')
	social_skype = fields.Char(related='website_id.social_skype')
        social_twitch = fields.Char(related='website_id.social_twitch')
        social_reddit = fields.Char(related='website_id.social_reddit')
        social_tumblr = fields.Char(related='website_id.social_tumblr')
        social_flickr = fields.Char(related='website_id.social_flickr')


