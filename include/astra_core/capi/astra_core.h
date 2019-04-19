/* THIS FILE AUTO-GENERATED FROM astra_core.h.lpp. DO NOT EDIT. */
#ifndef ASTRA_CAPI_H
#define ASTRA_CAPI_H

#include "astra_defines.h"
#include "astra_types.h"
#include "astra_core_version.h"
#include <stdbool.h>

ASTRA_BEGIN_DECLS

ASTRA_API astra_status_t astra_initialize();
ASTRA_API astra_status_t astra_terminate();

ASTRA_API astra_status_t astra_notify_plugin_event(astra_event_id id,
                                                   const void* data,
                                                   uint32_t dataSize);

ASTRA_API astra_status_t astra_streamset_is_available(astra_streamsetconnection_t connection,
                                                      bool* isAvailable);

ASTRA_API astra_status_t astra_streamset_open(const char* connectionString,
                                              astra_streamsetconnection_t* streamSet);

ASTRA_API astra_status_t astra_streamset_close(astra_streamsetconnection_t* streamSet);

ASTRA_API astra_status_t astra_streamset_get_uri(astra_streamsetconnection_t connection,
                                                 char* uri,
                                                 int32_t size);

ASTRA_API astra_status_t astra_reader_create(astra_streamsetconnection_t streamSet,
                                             astra_reader_t* reader);

ASTRA_API astra_status_t astra_reader_destroy(astra_reader_t* reader);

ASTRA_API astra_status_t astra_reader_get_stream(astra_reader_t reader,
                                                 astra_stream_type_t type,
                                                 astra_stream_subtype_t subtype,
                                                 astra_streamconnection_t* connection);

ASTRA_API astra_status_t astra_stream_get_description(astra_streamconnection_t connection,
                                                      astra_stream_desc_t* description);

ASTRA_API astra_status_t astra_stream_is_available(astra_streamconnection_t connection,
                                                   bool* isAvailable);

ASTRA_API astra_status_t astra_stream_start(astra_streamconnection_t connection);

ASTRA_API astra_status_t astra_stream_stop(astra_streamconnection_t connection);

ASTRA_API astra_status_t astra_reader_has_new_frame(astra_reader_t reader,
                                                    bool* hasNewFrame);

ASTRA_API astra_status_t astra_reader_open_frame(astra_reader_t reader,
                                                 int timeoutMillis,
                                                 astra_reader_frame_t* frame);

ASTRA_API astra_status_t astra_reader_close_frame(astra_reader_frame_t* frame);

ASTRA_API astra_status_t astra_reader_register_frame_ready_callback(astra_reader_t reader,
                                                                    astra_frame_ready_callback_t callback,
                                                                    void* clientTag,
                                                                    astra_reader_callback_id_t* callbackId);

ASTRA_API astra_status_t astra_reader_unregister_frame_ready_callback(astra_reader_callback_id_t* callbackId);

ASTRA_API astra_status_t astra_reader_get_frame(astra_reader_frame_t frame,
                                                astra_stream_type_t type,
                                                astra_stream_subtype_t subtype,
                                                astra_frame_t** subFrame);

ASTRA_API astra_status_t astra_stream_set_parameter(astra_streamconnection_t connection,
                                                    astra_parameter_id parameterId,
                                                    uint32_t inByteLength,
                                                    astra_parameter_data_t inData);

ASTRA_API astra_status_t astra_stream_get_parameter(astra_streamconnection_t connection,
                                                    astra_parameter_id parameterId,
                                                    uint32_t* resultByteLength,
                                                    astra_result_token_t* token);

ASTRA_API astra_status_t astra_stream_get_result(astra_streamconnection_t connection,
                                                 astra_result_token_t token,
                                                 uint32_t dataByteLength,
                                                 astra_parameter_data_t dataDestination);

ASTRA_API astra_status_t astra_stream_invoke(astra_streamconnection_t connection,
                                             astra_command_id commandId,
                                             uint32_t inByteLength,
                                             astra_parameter_data_t inData,
                                             uint32_t* resultByteLength,
                                             astra_result_token_t* token);

ASTRA_API astra_status_t astra_update();

ASTRA_END_DECLS

#endif /* ASTRA_CAPI_H */
